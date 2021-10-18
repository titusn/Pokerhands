import pytest

from deck import Deck

base_card_list = [
    'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'CT', 'CJ', 'CQ', 'CK',
    'CA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'DT', 'DJ', 'DQ',
    'DK', 'DA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'ST', 'SJ',
    'SQ', 'SK', 'SA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'HT',
    'HJ', 'HQ', 'HK', 'HA'
]


@pytest.fixture
def deck():
    return Deck()


def test_deck(deck):
    assert len(deck.get_deck()) == 52
    assert deck.show_all_cards() == base_card_list


def test_shuffle_deck(deck):
    deck.shuffle_deck()
    assert deck.show_all_cards() is not base_card_list
    assert set(deck.show_all_cards()) == set(base_card_list)
