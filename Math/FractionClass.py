def gcd(m,n):
    """
    gcd(m, n) = n if n divides m evenly.
    If n does not divide m evenly, answer = the greatest common divisor of n and the remainder of m divided by n.
    """
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __repr__(self):
        return "{}/{}".format(self.num, self.den)

    def __add__(self, other):
        """
        Fractions must have same denominator to be added.
        Here, we use the product of the two denominators as a common denominator.
        """
        num = (self.num * other.den) + (self.den * other.num)
        den = self.den * other.den
        common = gcd(num, den)
        return Fraction(num//common, den//common)

    def __sub__(self, other):
        num = (self.num * other.den) - (self.den * other.num)
        den = self.den * other.den
        common = gcd(num, den)
        return Fraction(num//common, den//common)

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den

        common = gcd(num, den)
        return Fraction(num//common, den//common)

    def __truediv__(self, other):
        num = self.num * other.den
        den = other.num * self.den

        common = gcd(num, den)
        return Fraction(num//common, den//common)

    def __eq__(self, other):
        first = self.num * other.den
        second = other.num * self.den

        return first == second


    def __lt__(self, other):
        first = self.num * other.den
        second = other.num * self.den

        return first < second

    def __gt__(self, other):
        first = self.num * other.den
        second = other.num * self.den

        return first > second




a = Fraction(2,3)
b = Fraction(3,5)

print(a+b)
print(a-b)
print(a*b)
print(a/b)