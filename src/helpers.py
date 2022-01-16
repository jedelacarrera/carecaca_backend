from typing import List
from src.models.card import Card
from src.enums import Rank


def get_last_card(played_cards: List[Card]) -> Card:
    last_card = played_cards[-1].copy()
    for card in played_cards[:-1][::-1]:
        if card.rank == last_card.rank:
            last_card.amount += 1
        else:
            break
    return last_card


def validate_new_play(played_cards: List[Card], new_cards: List[Card]) -> None:
    if len(new_cards) > 4 or len(new_cards) == 0:
        raise Exception("Deben ser entre 1 y 4 cartas")

    for card in new_cards:
        if card.rank != new_cards[0].rank:
            raise Exception("Todas las cartas deben ser del mismo tipo")

    if len(played_cards) == 0:
        return

    last_card = get_last_card(played_cards)
    new_card_rank = new_cards[0].rank
    print(last_card, last_card.rank.value, new_cards, new_card_rank.value)

    if new_card_rank == last_card.rank:
        if len(new_cards) + last_card.amount > 4:
            raise Exception("Máximo 4 cartas del mismo tipo seguidas")

    if (
        new_card_rank == Rank._10
        or new_card_rank == Rank._Jkr
        or new_card_rank == Rank._2
    ):
        return

    if last_card.rank == Rank._7 and new_card_rank.value > 7:
        raise Exception("Debe ser menor o igual a 7")
    elif last_card.rank == Rank._7:
        return

    if last_card.rank.value > new_card_rank.value:
        raise Exception("Debe ser mayor a la carta anterior")

    return


def does_complete_4(played_cards: List[Card], new_cards: List[Card]) -> bool:
    if len(played_cards) == 0 or len(new_cards) == 0:
        return False
    if get_last_card(played_cards).rank != get_last_card(new_cards).rank:
        return False
    return get_last_card(played_cards + new_cards).amount == 4


def should_empty_played_cards(played_cards: List[Card]) -> bool:
    last_card = get_last_card(played_cards)
    if last_card.amount == 4:
        return True

    if last_card.rank == Rank._10:
        return True

    return False


def remove_cards_from_list(cards: List[Card], origin: List[Card]) -> List[Card]:
    for card in cards:
        removed = False
        for index, origin_card in enumerate(origin):
            if card == origin_card:
                origin.pop(index)
                removed = True
                break
        if not removed:
            raise Exception("User doesn't have this card")
    return origin
