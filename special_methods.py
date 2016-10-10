import collections

# namedtuple can be used to build classes of objects that are just bundles of attributes with no custom methods, like a database record.
Card = collections.namedtuple('Card', ['rank', 'suit'])
beer_card = Card('7', 'diamonds')
# >>> Card(rank='7', suit='diamonds')


# Although FrenchDeck implicitly inherits from object, its functionality is not inherited, but comes from leveraging the Data Model and composition. By implementing the special methods __len__ and __getitem__ our FrenchDeck behaves like a standard Python sequence, allowing it to benefit from core language features — like iteration and slicing—and from the standard library, as shown by the examples using random.choice, reversed and sorted. Thanks to composition, the __len__ and __geti tem__ implementations can hand off all the work to a list object, self._cards.

class FrenchDeck:
        ranks = [str(n) for n in range(2, 11)] + list('JQKA')
        suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()

# Special methods are meant to be called by the Python interpreter, and not by you. You don’t write my_object.__len__(). You write len(my_object)
len(deck)

# __getitem__ method means we can get cards using following syntax
deck[0]
deck[-1]

# get the first three cards
deck[:3]

# pick just the aces by starting on index 12 and skipping 13 cards at a time
deck[12::13]

# iterate over deck
for card in deck:
    print(card)


# Should we create a method to pick a random card? No need. Python already has a function to get a random item from a sequence: random.choice. We can just use it on a deck instance:
from random import choice
choice(deck)

# Iteration is often implicit. If a collection has no __contains__ method, the in operator does a sequential scan. Case in point: in works with our FrenchDeck class because it is iterable.
Card('Q', 'hearts') in deck True



Pokemon = collections.namedtuple('Pokemon',['name','rank'])

class Team:
    def __init__(self, names, ranks):
        self._names = names
        self._ranks = ranks
        self._players = [Pokemon(name, rank) for name, rank in zip(self._names, self._ranks)]

    def __len__(self):
        return len(self._players)

    def __getitem__(self, position):
        return self._players[position]

    def __repr__(self):
        return 'Team(names=%s, ranks=%s)' % (self._names, self._ranks)



names = ['Abra','Kadabra','Alakazam','Mew']
ranks = [234,123,55,23]
team = Team(names=names, ranks=ranks)