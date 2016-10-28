from random import shuffle, randint, choice, random


STRING_TABLE = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
POPSIZE = 20


def fitness(source, target):
   fitval = 0
   for i in range(0, len(source)):
      fitval += abs(ord(target[i]) - ord(source[i]))
   return(fitval)


def generate_population(target):
    population = []
    for i in range(0, POPSIZE):
       dna = [choice(STRING_TABLE) for j in range(0, len(target))]
       fit = fitness(dna, target)
       candidate = {'dna': dna, 'fitness': fit }
       population.append(candidate)
    return population


def mutate(child_dna, target):
    # Mutate one position
    charpos = randint(0, len(child_dna) - 1)
    child_dna[charpos] = chr(ord(child_dna[charpos]) + randint(-1,1))
    child_fitness = fitness(child_dna, target)
    return child_dna, child_fitness


def crossover(parent1, parent2, target):
   child_dna = parent1['dna'][:]

   # Mix both DNAs
   start = randint(0, len(parent2['dna']) - 1)
   stop = randint(0, len(parent2['dna']) - 1)
   if start > stop:
      stop, start = start, stop
   child_dna[start:stop] = parent2['dna'][start:stop]

   # Mutate child
   child_dna, child_fitness = mutate(child_dna, target)
   return({'dna': child_dna, 'fitness': child_fitness})


def random_parents(population):
    """
    Uses uniform product distribution to ensure 'elitism':
    Parents towards the end of the population (highest fitness) are favored.
    """
    index = int(random() * random() * (POPSIZE - 1))
    parent1 = population[index]

    _population = population[:]
    _population.pop(index)
    index = int(random() * random() * (POPSIZE - 1))
    parent2 = _population[index]

    return parent1, parent2


def evolve(population, target):
    generation = 0
    while population[0]['fitness'] != 0:
        generation += 1
        print_population(generation, population)
        population.sort(key=lambda candidate: candidate['fitness'])

        parent1, parent2 = random_parents(population)
        child = crossover(parent1, parent2, target)
        if child['fitness'] < population[-1]['fitness']:
            population[-1] = child

def print_population(generation, population):
    for candidate in population:
        print("%6i %6i %15s" % (
            generation,
            candidate['fitness'],
            ''.join(candidate['dna'])
        ))

if __name__ == '__main__':

    target = "Hello, World!"

    population = generate_population(target)
    evolve(population, target)