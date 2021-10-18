from card import Card
from constants import CARD_VALUES


class Hand:
    def __init__(self, card_list: [str]):
        self.cards = [Card(c) for c in card_list]

    def find_high_card(self):
        highest_card = 0
        for card in self.cards:
            if CARD_VALUES.index(card.get_value()) > highest_card:
                highest_card = CARD_VALUES.index(card.get_value())
        return CARD_VALUES[highest_card]

    def find_pair(self):
        for card1 in self.cards:
            for card2 in self.cards:
                if card2 is card1:
                    continue
                if card1.get_value() == card2.get_value():
                    return card1.get_value()
        return None
