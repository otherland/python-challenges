from ast import parse
from sys import exc_info
from pyflakes.checker import Checker
from random import shuffle, randint, random, sample

# TABLE = [';', '=', '+', '-', '~', '*', '**', '/', '//', '<', '>', '==', '>=', '<=', '<>', '!=', 'is', 'is not', '+=', '-=', '*=', '/=', '%=', '&=', ',=', '^=', '<<=', '>>=', '**=', '//=', 'a', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
TABLE = ['a', ';', '=', '+', '-', '*', '**', '/', '//', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def get_sequence_index(sequence, string_index, separator):
    """
    Elements in sequence are joined by separator to create a string.
    string_index refers to an index in the string.
    Find the element in the original sequenceay that corresponds to the string_index.

    sequence = ['def', 'x', '?']
    separator = " "
    string = separator.join(sequence) >>> "def x ?"
    string_index = 6
    string[string_index] >>> "?"
    get_sequence_index(sequence, string_index, separator) >>> 2
    """
    count = 0
    string_index += 1
    sep = len(separator)
    for index, token in enumerate(sequence):
        size = len(token) + sep
        if count + size >= string_index:
            # found token
            return index
        count += size
    raise Exception('Failed to get sequence index.')


def get_fitness(tokens, check_warnings=True):
    separator = " "
    code = separator.join(tokens)
    fitness = 0
    error_indexes = list()

    try:
        tree = parse(code)
    except SyntaxError:
        error = exc_info()[1]
        lineno, offset, text = error.lineno -1, error.offset -1, error.text
        index = get_sequence_index(tokens, offset, separator)
        fitness += 50
        error_indexes = [index]
        return fitness, error_indexes

    if check_warnings:
        # Okay, it's syntactically valid.  Now check for warnings.
        result = Checker(tree, '<input>')
        fitness += len(result.messages)
        error_indexes = [get_sequence_index(tokens, m.col, separator) for m in result.messages]

    return fitness, error_indexes


def mutate(tokens, index, table, distance=1):
    _tokens = tokens[:]
    multiplier = 1
    if random() > 0.5:
        multiplier = -1
    offset = randint(1, distance) * multiplier

    token = _tokens[index]
    table_index = table.index(token)
    new_index = table_index + offset
    if new_index > len(table) - 1:
        new_index = offset
    _tokens[index] = table[new_index]
    return _tokens


def evolve(tokens, table):
    fitness, indexes = get_fitness(tokens)
    generation = 0
    while fitness != 0:
        generation += 1
        # mutate error tokens
        for index in indexes:
            tokens = mutate(tokens, index, table)
        fitness, indexes = get_fitness(tokens)
        print("%5i %5i %14s" % (generation, fitness, " ".join(tokens)))




def main():
    tokens = sample(TABLE, 6)
    evolve(tokens, TABLE)
if __name__ == '__main__':
    main()