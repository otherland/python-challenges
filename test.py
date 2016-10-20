import unittest

from heapsort import heapsort

class HeapsortTest(unittest.TestCase):
    def test(self):
        from random import sample
        sequence = list(range(15))
        shuffled = sample(sequence, len(sequence))
        self.assertEqual(heapsort(shuffled), sequence)

if __name__ == '__main__':
    unittest.main(buffer=True)