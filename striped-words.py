from re import split


# MY SOLUTION

def checkio(text):
    vowels, consonants = set('aeiouy'), set('bcdfghjklmnpqrstvwxz')
    text = [i for i in split('\W+', text.lower()) if i]
    count = 0
    for word in text:
        a, b = word[::2], word[1::2]
        if a and b and (vowels.issuperset(set(a)) and consonants.issuperset(set(b)) or consonants.issuperset(set(a)) and vowels.issuperset(set(b))):
            count += 1
    return count


# VEKY

def striped(word):
    """Is a word (encoded with d,v,c,p) striped?"""
    for forbidden in "d", "v"*2, "c"*2: # digit, double vowel, double consonant
        if forbidden in word:
            return False
    return len(word) > 1

def encode(text):
    """Generate kinds of letters for text (d,v,c,p)."""
    for char in text:
        if char.lower() in "aeiouy":
            yield "v"  # vowel
        elif char.isalpha():
            yield "c"  # consonant
        elif char.isdigit():
            yield "d"  # digit
        else:
            yield "p"  # punctuation (and space)

def checkio(text):
    """Number of striped words."""
    encoded = "".join(encode(text))
    # print encoded
    words = encoded.split("p")
    # print words
    result = sum(map(striped, words))
    # print result
    return result




# another solution

def checkio(text):
    encoded = ''.join('V' if t in 'AEIOUY' else
                      'C' if t.isalpha() else
                      'D' if t.isdigit() else
                      ' ' for t in text.upper())
    return sum('CC' not in t and
               'DD' not in t and
               'VV' not in t and
               len(t) > 1
               for t in encoded.split())

assert checkio("My name is ...") == 3

assert checkio("Hello world") == 0

assert checkio("A quantity of striped words.") == 1, "Only of"

assert checkio("Dog,cat,mouse,bird.Human.") == 3

assert checkio("To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it?") == 8

assert checkio("I can see dead people. yes,no.") == 2

assert checkio("z") == 0

