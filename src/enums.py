from enum import Enum
from typing import Any


class Suit(Enum):
    spade = "spade"
    club = "club"
    heart = "heart"
    diamond = "diamond"


class Rank(Enum):
    _Jkr = 1
    _2 = 2
    _3 = 3
    _4 = 4
    _5 = 5
    _6 = 6
    _7 = 7
    _8 = 8
    _9 = 9
    _10 = 10
    _J = 11
    _Q = 12
    _K = 13
    _A = 14


class CardOrigin(Enum):
    hand = "hand"
    hidden = "hidden"
    visible = "visible"

