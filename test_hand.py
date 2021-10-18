import pytest
from card import Card
from hand import Hand


def test_hand_init():
    test_hand = Hand(['R0'])
    assert isinstance(test_hand.cards[0], Card)


@pytest.mark.parametrize('hand,expected',
                         [(['C2', 'S4', 'D5', 'H9', 'H3'], '9'),
                          (['C2', 'S4', 'D5', 'H8', 'H3'], '8'),
                          (['C2', 'S4', 'DQ', 'HA', 'HK'], 'A')])
def test_find_high_card(hand, expected):
    test_hand = Hand(hand)
    assert test_hand.find_high_card() == expected


@pytest.mark.parametrize('hand,expected',
                         [(['C2', 'S4', 'D4', 'H9', 'H3'], '4'),
                          (['C2', 'S5', 'D5', 'H8', 'H3'], '5'),
                          (['C2', 'S4', 'D5', 'H9', 'H3'], None)])
def test_find_pair(hand, expected):
    test_hand = Hand(hand)
    assert test_hand.find_pair() == expected
