crazy_sum = lambda numbers: sum(index * element for index, element in enumerate(numbers))

assert crazy_sum([2]) == 0 # (2*0)
assert crazy_sum([2, 3]) == 3 # (2*0) + (3*1)
assert crazy_sum([2, 3, 5]) == 13 # (2*0) + (3*1) + (5*2)
assert crazy_sum([2, 3, 5, 2]) == 19 # (2*0) + (3*1) + (5*2) + (2*3)

crazy_nums = lambda n : [i for i in range(1, n) if (i % 5 == 0 and i % 3 != 0) or (i % 3 == 0 and i % 5 != 0)]
assert crazy_nums(3) == []
assert crazy_nums(10) == [3, 5, 6, 9]
assert crazy_nums(20) == [3, 5, 6, 9, 10, 12, 18]

square_nums = lambda n : sum(i*i for i in range(1, n))
def square_nums(n):
    count = 0
    for i in range(1, n):
        if i*i < n:
            count += 1
        else:
            break
    return count
assert square_nums(5) == 2
assert square_nums(10) == 3
assert square_nums(25) == 4


def openOrSenior(data):
    return ["Senior" if i[0] >= 55 and i[1] > 7 else "Open" for i in data ]

assert openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]]) == ['Open', 'Senior', 'Open', 'Senior']
assert openOrSenior([[16, 23],[73,1],[56, 20],[1, -1]]) == ['Open', 'Open', 'Senior', 'Open']