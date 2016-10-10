"""
A kidnapper wrote a ransom note but is worried it will be traced back to him. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use whole words available in the magazine, meaning he cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.
"""

from collections import Counter

def ransom_note(magazine, ransom):
    return (Counter(ransom) - Counter(magazine)) == {}


def ransom_note_2(magazine, ransom):
    words = {}
    for w in magazine:
        words[w] = words.get(w, 0) + 1
    for w in ransom:
        if words.get(w, 0) > 0:
            words[w] -= 1
        else:
            return False
    return True