import pygad
import numpy
import math 

import xlsxwriter

workbook = xlsxwriter.Workbook('coordinates.xlsx')
worksheet = workbook.add_worksheet()
floating_point_bordered = workbook.add_format({'num_format': '#,##0.0000000000', 'border': 1})
n = 7
dist_matrix = [[0, 2, 4.242640687, 3, 4.24, 1.414213562 , 1.414213562],
                [2,0, 3.16227766, 3.605551275, None, 1.414213562, 3.16227766],
                [4.242640687, 3.16227766, 0, 3, None, None, None],
                [3, 3.605551275, 3, 0, None, 4.123105626, 2.236067977],
                [4.24, None, None, None, 0, None, 3.390811112],
                [1.414213562, 1.414213562, None, 4.123105626, None, 0, 2.828427125],
                [1.414213562, 3.16227766, None, 2.236067977, 3.390811112, 2.828427125,	0]
]


def fitness_func(ga_instance, solution, solution_idx):
    xy_pair = []
    total_score = 0
    for i in range(len(solution)):
        x = dist_matrix[0][i] * math.cos(solution[i])
        y = dist_matrix[0][i] * math.sin(solution[i])
        xy_pair.append((x,y))
    output = 0
    for k in range(len(xy_pair)):
        cur = xy_pair[k]
        for j in range(k+1, len(xy_pair)):
            if dist_matrix[k][j]:
                comp = xy_pair[j]
                distance = math.sqrt((cur[0] - comp[0])**2 + (cur[1] - comp[1])**2)
                total_score += abs(dist_matrix[k][j] - distance)

    fitness = 1.0 / (total_score + 0.00001)
    return fitness


fitness_function = fitness_func

num_generations = 1000
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
                       init_range_low = 0,
                       init_range_high = 359,
                       parent_selection_type = "rws",
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes)


ga_instance.run()
solution, solution_fitness, solution_idx = ga_instance.best_solution()


xpoints = []
ypoints = []

for i in range(len(solution)):
    x = dist_matrix[0][i] * math.cos(solution[i])
    y = dist_matrix[0][i] * math.sin(solution[i])
    xpoints.append(x)
    ypoints.append(y)
    worksheet.write(i, 0, x, floating_point_bordered)
    worksheet.write(i, 1, y, floating_point_bordered)

    print("Coordinates: ", (x,y) )
print("Best Solution: ", solution)
print("solution_fitness: ", solution_fitness)

workbook.close()


import matplotlib.pyplot as plt
import numpy as np

plt.plot(xpoints, ypoints, 'o')
plt.show()