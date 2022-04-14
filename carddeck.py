import random

class Card:
    pass


class CardDeck: # base class: object
    SUITS = ['\u2663', '\u2666', '\u2665', '\u2660']
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, dealer):
        self.dealer = dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)


    @property
    def cards(self):
        return self._cards

    # getters/setters
    def get_dealer(self):
        return self._dealer

    # getter property
    @property
    def dealer(self):
        return self._dealer

    # setter property
    @dealer.setter
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a str")

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()
