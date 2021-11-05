from DuplicateCard import DuplicateCard
from InvalidHand import InvalidHand
from card import Card
from hand import Hand
from mamba import description, it
from expects import expect, equal, raise_error

with description('Hand'):
    with it('contains cards'):
        test_hand = Hand(['C2', 'C3', 'H4', 'HA', 'SK'])
        expect(type(test_hand.cards[0])).to(equal(Card))

with description('Hand contains cards'):
    with it('cannot contain the same card twice'):
        expect(lambda: Hand(['C2', 'C2', 'H4', 'HA', 'SK'])).to(raise_error(DuplicateCard))

    with it('must contain exactly 5 cards'):
        expect(lambda: Hand(['H1'])).to(raise_error(InvalidHand))
