from DuplicateCard import DuplicateCard
from InvalidHand import InvalidHand
from card import Card


class Hand:
    def __init__(self, card_list: [str]):
        if len(card_list) != 5:
            raise InvalidHand('Poker hands must consist of exactly 5 cards')
        elif len(card_list) != len(set(card_list)):
            raise DuplicateCard('Cannot contain the same card twice')
        else:
            self.cards = [Card(c) for c in card_list]
