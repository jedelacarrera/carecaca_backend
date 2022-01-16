from typing import Dict, List
from src.models.card import Card
from src.enums import CardOrigin
from src.helpers import remove_cards_from_list


class Player:
    username: str
    hand: List[Card]
    hidden: List[Card]
    visible: List[Card]

    def __init__(
        self, username: str, hand: List[Dict], visible: List[Dict], hidden: List[Dict]
    ):
        self.username = username
        self.hand = [Card(**card_dict) for card_dict in hand]
        self.visible = [Card(**card_dict) for card_dict in visible]
        self.hidden = [Card(**card_dict) for card_dict in hidden]

    @property
    def is_finished(self):
        if len(self.hand) > 0:
            return False
        if len(self.visible) > 0:
            return False
        if len(self.hidden) > 0:
            return False
        return True

    def to_json(self):
        return {
            "username": self.username,
            "hand": [card.to_json() for card in sorted(self.hand)],
            "visible": [card.to_json() for card in self.visible],
            "hidden": [card.to_json() for card in self.hidden],
        }

    def remove_cards(self, cards: List[Card], origin: CardOrigin):
        if origin == CardOrigin.hand:
            self.hand = remove_cards_from_list(cards, self.hand)
            return

        if origin == CardOrigin.visible and len(self.hand) == 0:
            self.visible = remove_cards_from_list(cards, self.visible)
            return

        if (
            origin == CardOrigin.hidden
            and len(self.visible) == 0
            and len(self.hand) == 0
        ):
            self.hidden = remove_cards_from_list(cards, self.hidden)
            return

        raise Exception("Not a valid origin of cards!")

    def take_cards_from_deck(self, deck: List[Card], max_cards) -> None:
        if len(deck) == 0 or len(self.hand) >= max_cards:
            return

        cards_to_take = max_cards - len(self.hand)
        if len(deck) < cards_to_take:
            cards_to_take = len(deck)

        for _ in range(cards_to_take):
            self.hand.append(deck.pop())

