"""
We define the rating for Alice's challenge to be the triplet , and the rating for Bob's challenge to be the triplet .

Your task is to find their comparison scores by comparing with , with , and with .

    If a[0] > b[0], then Alice is awarded point.
    If a[0] < b[0], then Bob is awarded point.
    If a[0] == b[0], then neither person receives a point.
"""

a = (5, 6, 7)
b = (3, 6, 10)

s1 = 0
s2 = 0

for i in range(len(a)):
    if a[i] == b[i]:
        continue
    elif a[i] > b[i]:
        s1 += 1
    else:
        s2 += 1

print(s1, s2)
