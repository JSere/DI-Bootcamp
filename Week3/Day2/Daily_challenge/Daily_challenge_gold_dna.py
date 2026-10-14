import random

class Gene:
    def __init__(self, value=None):
        self.value = value if value is not None else random.choice([0, 1])

    def mutate(self):
        self.value = 1 - self.value


class Chromosome:
    def __init__(self):
        self.genes = [Gene() for _ in range(3)]

    def mutate(self):
        for gene in self.genes:
            if random.random() < 0.5:
                gene.mutate()

    def is_perfect(self):
        return all(gene.value == 1 for gene in self.genes)


class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(3)]

    def mutate(self):
        for chromosome in self.chromosomes:
            if random.random() < 0.5:
                chromosome.mutate()

    def is_perfect(self):
        return all(chrom.is_perfect() for chrom in self.chromosomes)


class Organism:
    def __init__(self, dna, environment_prob):
        self.dna = dna
        self.environment_prob = environment_prob

    def mutate(self):
        if random.random() < self.environment_prob:
            self.dna.mutate()

    def is_perfect(self):
        return self.dna.is_perfect()


population_size = 50
environment_probability = 0.9
population = [Organism(DNA(), environment_probability) for _ in range(population_size)]

generations = 0
found = False

print("Starting evolutionary simulation...")

while not found:
    generations += 1
    
    if generations % 1000 == 0:
        print(f"Generation {generations} in progress...")
        
    for organism in population:
        organism.mutate()
        if organism.is_perfect():
            found = True
            break

print(f"\nTarget reached! An organism evolved a DNA made entirely of 1s in {generations} generations.")