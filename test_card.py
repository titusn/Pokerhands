from card import Card


def test_card_has_suit_and_value():
  test_card = Card('R0')
  assert test_card.get_suit() == 'R'
  assert test_card.get_value() == '0'