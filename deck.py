import random
from card import Card
from constants import CARD_VALUES, CARD_SUITS


class Deck:
    def __init__(self, card_values = CARD_VALUES, card_suits = CARD_SUITS):
        self.card_list = list()
        self.cards = list()
        for suit in card_suits:
            suit = suit * len(card_values)
            card_set = [a + b for a, b in zip(suit, card_values)]
            self.card_list.extend(card_set)
        for card in self.card_list:
            self.cards.append(Card(card)) 

    def shuffle_deck(self):
        random.shuffle(self.cards)
    
    def get_deck(self):
        return self.cards
    
    def show_all_cards(self) -> [str]:
        card_list = list()
        for card in self.cards:
            card_list.append(card.card)
        return card_list
