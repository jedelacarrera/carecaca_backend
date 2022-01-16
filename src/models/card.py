from typing import List, Optional
from src.enums import Suit, Rank
import random


class Card:
    rank: Rank
    suit: Optional[Suit]
    amount: int

    def __init__(self, rank, suit, amount: int = 1):
        if isinstance(rank, str):
            if rank[0] != "_":
                rank = "_" + rank
            rank = Rank[rank]
        if isinstance(suit, str):
            suit = Suit[suit]

        self.rank = rank
        self.suit = suit
        self.amount = amount

    def to_json(self):
        if self.amount != 1:
            return {
                "rank": self.rank.name[1:],
                "suit": self.suit.name if self.suit else None,
                "amount": self.amount,
            }
        return {
            "rank": self.rank.name[1:],
            "suit": self.suit.name if self.suit else None,
        }

    def __eq__(self, other: "Card") -> bool:
        if self.rank.name != other.rank.name:
            return False
        if self.amount != other.amount:
            return False
        if self.suit is None and other.suit is None:
            return True
        if self.suit.name != other.suit.name:
            return False
        return True

    def __lt__(self, other: "Card") -> bool:
        return self.rank.value < other.rank.value

    def copy(self):
        return Card(**self.to_json())

    def __repr__(self) -> str:
        return f"<Card {str(self.amount) + '*' if self.amount != 1 else ''}{self.rank.name}{self.suit and self.suit.name}>"

    @staticmethod
    def shuffled_cards() -> List["Card"]:  # 2 decks
        jkr1 = Card(rank=Rank._Jkr, suit=None)
        jkr2 = Card(rank=Rank._Jkr, suit=None)
        jkr3 = Card(rank=Rank._Jkr, suit=None)
        jkr4 = Card(rank=Rank._Jkr, suit=None)

        cards = [jkr1, jkr2, jkr3, jkr4]
        for suit in Suit:
            for rank in Rank:
                if rank == Rank._Jkr:
                    continue
                card_blue = Card(rank=rank, suit=suit)
                card_red = Card(rank=rank, suit=suit)
                cards.append(card_blue)
                cards.append(card_red)
        random.shuffle(cards)
        return cards
