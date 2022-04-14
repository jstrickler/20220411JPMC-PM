from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck() # call in parent...
        for joker_number in '1', '2':
            joker = joker_number, "\U0001F0CF"
            self._cards.append(joker)


