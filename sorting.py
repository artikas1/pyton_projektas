import random
import time

def initialize_population(data):
    population = [random.sample(data, len(data)) for _ in range(10)]
    return population

def fitness(individual):
    return sum(1 for i in range(len(individual)) if individual[i][0] == i)

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point] + [gene for gene in parent2 if gene not in parent1[:crossover_point]]
    return child

def mutate(individual):
    mutation_point1, mutation_point2 = random.sample(range(len(individual)), 2)
    individual[mutation_point1], individual[mutation_point2] = individual[mutation_point2], individual[mutation_point1]

def genetic_sort(data, generations=100):
    population = initialize_population(data)

    for generation in range(generations):
        population = sorted(population, key=fitness)
        best_individual = population[0]

        if fitness(best_individual) == len(best_individual):
            break

        new_population = [best_individual]

        for _ in range(len(population) - 1):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)

        population = new_population

    return best_individual

# Read data from the text file
file_path = 'unsorted_dataset.txt'  # Replace with the actual path to your text file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Parse the data
data = [line.strip().split(',') for line in lines]

# Convert the first column to float for sorting
data = [(float(row[0]), row) for row in data]

# Measure time taken by genetic algorithm
start_time = time.time()
result = genetic_sort(data)
genetic_time = time.time() - start_time

# Write the sorted result to a file
output_file_path = 'sorted_dataset.txt'
with open(output_file_path, 'w') as output_file:
    for _, row in result:
        output_file.write(','.join(row) + '\n')

# Print the sorted result
print(f"Sorted result written to '{output_file_path}'")

# Print the time taken by the genetic algorithm
print(f"Genetic Algorithm Time: {genetic_time} seconds")
