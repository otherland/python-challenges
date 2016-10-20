#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on
# different floors of a five-floor apartment building.
#
# Hopper does not live on the top floor.
# Kay does not live on the bottom floor.
# Liskov does not live on either the top or the bottom floor.
# Perlis lives on a higher floor than does Kay.
# Ritchie does not live on a floor adjacent to Liskov's.
# Liskov does not live on a floor adjacent to Kay's.
#
# Where does everyone live?
#
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay,
# Liskov, Perlis, and Ritchie.

import itertools

Hopper, Kay, Liskov, Perlis, Ritchie = ['Hopper', 'Kay', 'Liskov', 'Perlis', 'Ritchie']

def floor_puzzle():
    # Your code here
    people = [Hopper, Kay, Liskov, Perlis, Ritchie]
    combi = itertools.permutations(people)
    for poss in combi:
        indexes = [poss.index(i) for i in people]
        H, K, L, P, R = indexes
        if H != 4 and K != 0 and L != 0 and L != 4 and P > K and abs(R-L) != 1 and abs(L-K) != 1:
            return indexes
print(floor_puzzle())