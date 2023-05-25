# __main__.py
"""
    an attempt to implement Genetic Algorithm using first example in
    Lec 2 Genetic algorithm.pptx
"""
import random, sys

# set hyperparameters
N = 100 # population size
pc = 0.8 # probability of crossover
pm = 0.2 # probability of mutation
elitism = 2 # Elitism

def initialize_population(n: int) -> list:
    """Initialization step"""

    value_list = [round((1 + ((16 - 1) / (2**6 -1)) * random.uniform(1.0, 16.0)), 8) for _ in range(n)]
    return value_list

def fitness(chromosomes: float) -> float:
    """Fitness function"""

    return chromosomes ** 0.5

def Roulette_wheel_selection(population: list, fitness_list: list) -> list:
    """Selection step"""

    total_fitness = sum(fitness_list)
    pf_list = [c / total_fitness for c in population]
    sellection_list = []
    for _ in range(len(population)):
        i = random.random()
        cpf = 0
        for pf in pf_list:
            cpf += pf
            if cpf >= i:
                sellection_list.append(population[pf_list.index(pf)])
    return sellection_list

def intermediate_recombination(sellection_list: list) -> list:
    """Crossover step"""

    offspring_list = []
    for p in range(3):
        r = random.random()
        if r < pc:
            for f in range(2):
                y = random.uniform(-0.25, 1.24)
                offspring = sellection_list[p + f] + y * (sellection_list[(p + f) + 1] - sellection_list[p + f])
                offspring = round((1 + ((16 - 1) / (2**6 -1)) * offspring), 8)
                offspring_list.append(offspring)
        else:
            offspring_list.append(sellection_list[p])
            offspring_list.append(sellection_list[p+1])
    return offspring_list

def mutation_func(offsprings: list) -> list:
    """Mutation step"""

    new_offsprings = []
    for offspring in offsprings:
        r = random.random()
        if r < pm:
            r_c = round((1 + ((16 - 1) / (2**6 -1)) * random.uniform(1.0, 16.0)), 8)
            new_offsprings.append(r_c)
        else:
            new_offsprings.append(offspring)
    return new_offsprings

def replace_func(population: list, population_fitness: list, offsprings: list, offsprings_fitness: list) -> list:
    """Replace step"""

    indx_1 = population_fitness.index(min(population_fitness))
    population_fitness.remove(min(population_fitness))
    indx_2 = population_fitness.index(min(population_fitness))
    population_fitness.remove(min(population_fitness))

    offspring_indx1 = offsprings_fitness.index(max(offsprings_fitness))
    offsprings_fitness.remove(max(offsprings_fitness))
    offspring_indx2 = offsprings_fitness.index(max(offsprings_fitness))
    offsprings_fitness.remove(max(offsprings_fitness))

    new_population = offsprings.copy()
    new_population[offspring_indx1] = population[indx_1]
    new_population[offspring_indx2] = population[indx_2]

    return new_population

def main() -> None:
    """Main function"""

    population = initialize_population(N) # initialization
    

    for g in range(100_000_000):
        population_fitness = [fitness(i) for i in population]

        best_indx = population_fitness.index(min(population_fitness))
        print(f'The best chromosome in generation {g} -> {population[best_indx]}, fitness = {population_fitness[best_indx]}')

        sellection_list = Roulette_wheel_selection(population, population_fitness) # selection

        offsprings = intermediate_recombination(sellection_list) # Crossover

        offsprings = mutation_func(offsprings) # Mutation

        offsprings_fitness = [fitness(i) for i in offsprings]

        population = replace_func(population, population_fitness.copy(), offsprings, offsprings_fitness.copy()) # Replace


if __name__ == "__main__":
    main()
