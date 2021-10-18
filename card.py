class Card:
    def __init__(self, card: str):
        self.card = card

    def get_value(self) -> str:
        return self.card[1]

    def get_suit(self) -> str:
        return self.card[0]
