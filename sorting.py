import random
import re
import numpy as np

# Function to extract the specified field from a row
def get_field(row, field_index):
    # Split the row by commas
    row_values = row.split(',')

    # Extract the field value
    field_value = row_values[field_index].strip()

    # If the field is a URL, remove commas within the URL
    if field_index == 11:  # Assuming the URL is in the 11th column
        field_value = re.sub(r'https?://', '', field_value)  # Remove commas from the URL

    return field_value

# Function to calculate the fitness of an individual (a permutation of indices)
def calculate_fitness(individual, dataset, field_index):
    sorted_indices = sorted(range(len(dataset)), key=lambda i: float(get_field(dataset[i], field_index)))
    return sum(abs(i - j) for i, j in zip(sorted_indices, individual))

# Function to read the dataset from a text file
def read_dataset(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

# Function to write the sorted dataset to a text file
def write_sorted_dataset(sorted_dataset, file_path):
    with open(file_path, 'w') as file:
        file.writelines(sorted_dataset)

# Get user input for selecting the field for sorting
sort_field_index = int(input("Enter the index of the field by which you want to sort the dataset: ")) - 1

# Get user input for the file path of the dataset
file_path = "unsorted_dataset.txt"

# Read the dataset from the text file
dataset = read_dataset(file_path)

# Genetic algorithm parameters
population_size = 100
mutation_rate = 0.02
generations = 200

# Create an initial population of individuals
population = [list(range(len(dataset))) for _ in range(population_size)]

# Main genetic algorithm loop
for generation in range(generations):
    # Evaluate the fitness of each individual in the population
    fitness_scores = [calculate_fitness(individual, dataset, sort_field_index) for individual in population]

    # Select individuals for reproduction based on fitness
    selected_indices = sorted(range(len(fitness_scores)), key=lambda k: fitness_scores[k])[:10]
    selected_population = [population[i] for i in selected_indices]

    # Create the next generation through crossover
    offspring = []
    for _ in range(population_size - len(selected_population)):
        parent1, parent2 = random.sample(selected_population, 2)
        crossover_point = random.randint(0, len(parent1))
        child = parent1[:crossover_point] + parent2[crossover_point:]
        offspring.append(child)

    # Mutate some individuals
    for child in offspring:
        if random.random() < mutation_rate:
            index1, index2 = random.sample(range(len(child)), 2)
            child[index1], child[index2] = child[index2], child[index1]

    # Replace the old population with the new generation
    population = selected_population + offspring

# Get the best individual (permutation) from the final population
best_individual = min(population, key=lambda individual: calculate_fitness(individual, dataset, sort_field_index))

# Use argsort from NumPy to get the indices that would sort the field
sorted_indices = np.argsort([float(get_field(dataset[i], sort_field_index)) for i in range(len(dataset))])

# Sort the dataset based on the sorted indices
sorted_dataset = [dataset[i] for i in sorted_indices]

# Get user input for the file path to save the sorted dataset
output_file_path = "sorted.txt"

# Clear the content of the file
with open(output_file_path, 'w'):
    pass

# Write the sorted dataset to a text file
write_sorted_dataset(sorted_dataset, output_file_path)


print(f"The sorted dataset has been saved to {output_file_path}.")
