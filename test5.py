import random

POPULATION_SIZE = 100
GENES = '''abcdefghijklmnopqrstuvwcyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''
TARGET = "Archi Mehta"

class Individual(object):
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()

    @classmethod
    def mutated_genes(cls):
        '''Create random genes for mutation'''
        return random.choice(GENES)

    @classmethod
    def create_gnome(cls):
        '''Create a random chromosome (gnome)'''
        gnome_len = len(TARGET)
        return [cls.mutated_genes() for _ in range(gnome_len)]

    def mate(self, par2):
        '''Mate with another individual to create offspring'''
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):
            prob = random.random()
            if prob < 0.45:
                child_chromosome.append(gp1)
            elif prob < 0.90:
                child_chromosome.append(gp2)
            else:
                child_chromosome.append(self.mutated_genes())
        return Individual(child_chromosome)

    def cal_fitness(self):
        '''Calculate fitness score'''
        fitness = 0
        for gs, gt in zip(self.chromosome, TARGET):
            if gs != gt:
                fitness += 1
        return fitness

# Main genetic algorithm loop
generation = 1
found = False
population = []

# Create initial population
for _ in range(POPULATION_SIZE):
    gnome = Individual.create_gnome()
    population.append(Individual(gnome))

while not found:
    population = sorted(population, key=lambda x: x.fitness)

    print("Generation: {}\tString: {}\tFitness: {}".format(
        generation,
        "".join(population[0].chromosome),
        population[0].fitness
    ))

    if population[0].fitness <= 0:
        found = True
        break

    new_generation = []
    s = int((10 * POPULATION_SIZE) / 100)
    new_generation.extend(population[:s])

    s = int((90 * POPULATION_SIZE) / 100)
    for _ in range(s):
        parent1 = random.choice(population[:50])
        parent2 = random.choice(population[:50])
        child = parent1.mate(parent2)
        new_generation.append(child)

    population = new_generation
    generation += 1