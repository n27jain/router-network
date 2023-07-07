import pygad
import numpy
import math 
n = 7
dist_matrix = []



desired_output = 44

def fitness_func(ga_instance, solution, solution_idx):
    xy_pair = []
    total_score = 0
    for i in range(len(solution)):
        x = dist_matrix[0][i] * math.cos(solution[i])
        y = dist_matrix[0][i] * math.sin(solution[i])
        xy_pair.append((x.y))
    output = 0
    for k in range(len(xy_pair)):
        cur = xy_pair[k]
        for j in range(k+1, len(xy_pair)):
            comp = xy_pair[j]
            distance = math.sqrt((cur[0] - comp[0])**2 + (cur[1] - comp[1])**2)
            total_score += abs(dist_matrix[k][j] - distance)

    fitness = 1.0 / (total_score + 0.00001)
    return fitness


fitness_function = fitness_func

num_generations = 50
num_parents_mating = 4

sol_per_pop = 8
num_genes = n

init_range_low = -2
init_range_high = 5

parent_selection_type = "sss"
keep_parents = 1

crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 10


ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       init_range_low=init_range_low,
                       init_range_high=init_range_high,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes)


ga_instance.run()
solution, solution_fitness, solution_idx = ga_instance.best_solution()

print("Best Solution: ", solution)