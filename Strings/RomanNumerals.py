"""
Symbols are placed from left to right in order of value, starting with the largest. However, in a few specific cases,[2] to avoid four characters being repeated in succession (such as IIII or XXXX), subtractive notation is often used as follows:[3][4]

    I placed before V or X indicates one less, so four is IV (one less than five) and nine is IX (one less than ten)
    X placed before L or C indicates ten less, so forty is XL (ten less than fifty) and ninety is XC (ten less than a hundred)
    C placed before D or M indicates a hundred less, so four hundred is CD (a hundred less than five hundred) and nine hundred is CM (a hundred less than a thousand)[5]
"""


def roman_to_int(roman):
    map = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    }
    ints = [map[i] for i in roman]
    prev = calc = ints[0]
    for curr in ints[1:]:
        if prev and curr > prev:
            calc += curr - prev - prev
            curr = 0
            prev = 0
        else:
            calc += curr
            prev = curr
    return calc


def int_to_roman(number):
    sym = list('MDCLXVI')
    ints = list(map(int, list(str(number))))
    offset = (4 - len(ints) ) * 2
    h = zip(sym[offset::2], ints)
    j = []
    for i in h:
        if i[1] == 4:
            j.append(i[0] + sym[offset-1])
        elif i[1] == 9:
            j.append(i[0] + sym[offset-2])
        elif i[1] == 5:
            j.append(sym[offset-1])
        elif i[1] > 5:
            j.append(sym[offset-1] + i[0] * (i[1] - 5))
        else:
            j.append(i[0] * i[1])
        offset += 2
    return ''.join(j)

# print int_to_roman(50)
# print int_to_roman(499)
# print int_to_roman(3888)




"MY SOLUTIONS ABOVE"



def int_to_roman(number):
    result = ''
    pairs = [
     (1000, 'M'),
     (900, 'CM'),
     (500, 'D'),
     (400, 'CD'),
     (100, 'C'),
     (90, 'XC'),
     (50, 'L'),
     (40, 'XL'),
     (10, 'X'),
     (9, 'IX'),
     (5, 'V'),
     (4, 'IV'),
     (1, 'I')
    ]
    for arabic, roman in pairs:
        result += number // arabic * roman
        number %= arabic
    return result



def int_to_roman(number):
    pairs = [
     (1000, 'M'),
     (900, 'CM'),
     (500, 'D'),
     (400, 'CD'),
     (100, 'C'),
     (90, 'XC'),
     (50, 'L'),
     (40, 'XL'),
     (10, 'X'),
     (9, 'IX'),
     (5, 'V'),
     (4, 'IV'),
     (1, 'I')
    ]
    result = ""

    for arab, roman in pairs:
        if number <= 0:
            break
        if number >= arab:
            result += roman
            number -= arab
    return result


print int_to_roman(50)