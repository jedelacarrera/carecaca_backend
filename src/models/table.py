import os
import time
import json
from typing import Dict, Any, List
from src.enums import CardOrigin, Suit, Rank
from src.models.card import Card
from src.models.player import Player
from src.helpers import validate_new_play, does_complete_4, should_empty_played_cards


class Table:
    CARDS_PER_PLAYER = 4

    table_name: str
    filename: str
    path: str
    players: List[Player]
    deck: List[Card]
    played_cards: List[Card]
    username_turn: str
    clockwise: bool
    finished_usernames: List[str]

    def __init__(self, table_name: str, filename: str):
        self.table_name = table_name
        self.filename = filename
        self.path = f"tmp/{table_name}/{filename}"

        with open(self.path, "r") as file:
            table_dict = json.load(file)

        self.started = table_dict["started"]
        self.username_turn = table_dict["username_turn"]
        self.clockwise = table_dict["clockwise"]
        self.finished_usernames = table_dict.get("finished_usernames", [])
        self.played_cards = [
            Card(**card_dict) for card_dict in table_dict["played_cards"]
        ]
        self.deck = [Card(**card_dict) for card_dict in table_dict["deck"]]
        self.players = [Player(**player_dict) for player_dict in table_dict["players"]]

    @staticmethod
    def load_from_folder(table_name: str) -> "Table":
        if not os.path.isdir("tmp"):
            os.mkdir("tmp")
        path = f"tmp/{table_name}/"
        if not os.path.isdir(path):
            os.mkdir(path)

        files = os.listdir(path)

        if len(files) == 0:
            Table._create_table(path)
            files = os.listdir(path)

        return Table(table_name, sorted(files)[-1])

    @staticmethod
    def _create_table(path: str) -> None:
        filename = str(time.time()) + ".json"
        with open(path + filename, "w") as file:
            json.dump(
                {
                    "players": [],
                    "started": False,
                    "played_cards": [],
                    "deck": [],
                    "username_turn": None,
                    "clockwise": True,
                    "finished_usernames": [],
                },
                file,
                indent=4,
            )

    def to_json(self) -> Dict[str, Any]:
        return {
            "players": [player.to_json() for player in self.players],
            "started": self.started,
            "played_cards": [card.to_json() for card in self.played_cards],
            "deck": [card.to_json() for card in self.deck],
            "username_turn": self.username_turn,
            "clockwise": self.clockwise,
            "finished_usernames": self.finished_usernames,
        }

    def to_output_request(self) -> Dict[str, Any]:
        json_dict = self.to_json()
        json_dict["deck"] = len(self.deck)
        return json_dict

    def save(self):
        filename = f"tmp/{self.table_name}/" + str(time.time()) + ".json"
        with open(filename, "w") as file:
            content = self.to_json()
            json.dump(content, file, indent=4)

    def deal(self):
        if self.started:
            return
        shuffled_cards = Card.shuffled_cards()
        if len(self.players) * Table.CARDS_PER_PLAYER * 3 > len(shuffled_cards):
            raise Exception("Too many players")

        for player in self.players:
            for _ in range(Table.CARDS_PER_PLAYER):
                player.hand.append(shuffled_cards.pop())
                player.hidden.append(shuffled_cards.pop())
                player.visible.append(shuffled_cards.pop())
        self.played_cards = []
        self.deck = shuffled_cards
        self.started = True
        self.username_turn = self.players[0].username
        self.save()

    def add_player(self, username):
        for player in self.players:
            if player.username == username:
                return
        if self.started:
            raise Exception("Game already started")
        player = Player(username=username, hand=[], hidden=[], visible=[])
        self.players.append(player)
        self.save()

    def find_player_index_by_username(self, username: str) -> int:
        for (index, player) in enumerate(self.players):
            if player.username == username:
                return index
        raise Exception("User doesn't exist")

    def play_cards(self, new_cards: List[Card], username: str, origin: CardOrigin):
        validate_new_play(self.played_cards, new_cards)

        if username != self.username_turn and not does_complete_4(
            self.played_cards, new_cards
        ):
            raise Exception("No es tu turno")

        self.played_cards += new_cards
        if new_cards[0].rank == Rank._J:
            self.clockwise = not self.clockwise

        player_index = self.find_player_index_by_username(username)
        player = self.players[player_index]
        player.remove_cards(new_cards, origin)
        player.take_cards_from_deck(self.deck, Table.CARDS_PER_PLAYER)

        new_player_index = player_index + 1 if self.clockwise else player_index - 1
        self.username_turn = self.players[new_player_index % len(self.players)].username

        # handle player with no cards
        if player.is_finished:
            self.finished_usernames.append(player.username)
            self.players.pop(player_index)

        if should_empty_played_cards(self.played_cards):
            self.played_cards = []
            # Turn is to the previous player
            player_index = self.find_player_index_by_username(self.username_turn)
            # Contrary to play_cards method, the previous player starts
            new_player_index = player_index - 1 if self.clockwise else player_index + 1
            self.username_turn = self.players[
                new_player_index % len(self.players)
            ].username

        self.save()

    def play_cards_or_take_played_cards(
        self, new_cards: List[Card], username: str, origin: CardOrigin
    ):
        try:
            self.play_cards(new_cards, username, origin)
            return "correctamente"
        except Exception:
            pass

        self.played_cards += new_cards
        player_index = self.find_player_index_by_username(username)
        player = self.players[player_index]
        player.remove_cards(new_cards, origin)
        self.take_played_cards(username)
        return "incorrectamente, se llevó el montón"

    def take_played_cards(self, username: str):
        player_index = self.find_player_index_by_username(username)
        self.players[player_index].hand += self.played_cards
        self.played_cards = []
        # Contrary to play_cards method, the previous player starts
        new_player_index = player_index - 1 if self.clockwise else player_index + 1
        self.username_turn = self.players[new_player_index % len(self.players)].username
        self.save()
