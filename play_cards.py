from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Nellie")
print(d1)
d2 = CardDeck("Andy")
print(d2)

print(d1.get_dealer())
print(d1.dealer)

d1.dealer = "Ferdinand"
print(d1.dealer)

try:
    d1.dealer = 123.4
except TypeError as err:
    print(err)
else:
    print(d1.dealer)

d1.shuffle()
print(d1.cards)
print('-' * 60)
j = JokerDeck("Franny")
print(j)
j.shuffle()
print(j.cards)










