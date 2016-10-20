import sys
n = int(input())
items = [input().split() for _ in range(n)]
book = dict(items)

# Unknown number of inputs remaining, strip newlines
queries = map(lambda x: x.strip(), sys.stdin.readlines())

for name in queries:
    if name in book:
        print("{}={}".format(name, book[name]))
    else:
        print("Not found")

"""
Task
    Given names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for is not found, print Not found instead.

Input Format

    The first line contains an integer, , denoting the number of entries in the phone book.
    Each of the subsequent lines describes an entry in the form of space-separated values on a single line. The first value is a friend's name, and the second value is an -digit phone number.

    After the lines of phone book entries, there are an unknown number of lines of queries. Each line (query) contains a to look up, and you must continue reading lines until there is no more input.


Output Format

    On a new line for each query, print Not found if the name has no corresponding entry in the phone book; otherwise, print the full and in the format name=phoneNumber.

Sample Input

    3
    sam 99912222
    tom 11122222
    harry 12299933
    sam
    edward
    harry

Sample Output

    sam=99912222
    Not found
    harry=12299933

Explanation

    We add the following (Key,Value) pairs to our map so it looks like this:

    We then process each query and print key=value if the queried is found in the map; otherwise, we print Not found.

    Query 0: sam
    Sam is one of the keys in our dictionary, so we print sam=99912222.

    Query 1: edward
    Edward is not one of the keys in our dictionary, so we print Not found.

    Query 2: harry
    Harry is one of the keys in our dictionary, so we print harry=12299933.
"""