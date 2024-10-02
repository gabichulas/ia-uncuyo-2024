import random
import time
import math
import numpy as np

def init_board(n):
    return [random.randint(0, n-1) for _ in range(n)]

def h(board):
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def get_neighbors(board):
    neighbors = []
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i] != j:
                neighbor = board[:]
                neighbor[i] = j
                neighbors.append(neighbor)
    return neighbors

# Hill Climbing

def hill_climbing(n, max_iterations = 1000):
    current_board = init_board(n)
    current_conflicts = h(current_board)
    states_explored = 0
    start = time.time()
    
    while states_explored < max_iterations:
        neighbors = get_neighbors(current_board)
        next_board = None
        next_conflicts = current_conflicts
        
        for neighbor in neighbors:
            conflicts = h(neighbor)
            states_explored += 1
            if conflicts < next_conflicts:
                next_board = neighbor
                next_conflicts = conflicts
        
        if next_conflicts >= current_conflicts:
            break
        
        current_board = next_board
        current_conflicts = next_conflicts

    end = time.time()
    final_time = end - start

    return current_board, states_explored, final_time, current_conflicts

# Simulated Annealing

def schedule(t): return 1/t

def prob(delta_e, t):
    if delta_e < 0:
        return 1.0
    else:
        return math.exp(-delta_e / t)

def simulated_annealing(n, max_iterations = 1000):
    initial_temperature = 1000
    final_temperature = 1
    cooling_rate = 0.99  
    states_explored = 0

    current_board = init_board(n)

    temperatures = np.arange(initial_temperature, final_temperature, -cooling_rate)
    
    start = time.time()

    for t in temperatures:
        temp = schedule(t)
        current_neighbors = get_neighbors(current_board)
        new_board = random.choice(current_neighbors)
        delta_e = h(new_board) - h(current_board)

        states_explored += 1
        if delta_e < 0 or random.random() < prob(delta_e, temp):
            current_board = new_board
        if h(current_board) == 0: break
        if states_explored >= max_iterations: break
    
    end = time.time()

    final_time = end - start

    return current_board, states_explored, final_time, h(current_board)

# GA

def fitness(board): return -h(board)

def select(population, fitnesses):
    total_fitness = sum(fitnesses)
    probabilities = [f / total_fitness for f in fitnesses]
    return population[np.random.choice(len(population), p=probabilities)]

def crossover(parent1, parent2):
    n = len(parent1)
    crossover_point = random.randint(0, n-1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(board, mutation_rate = 0.1):
    n = len(board)
    for i in range(n):
        if random.random() < mutation_rate:
            board[i] = random.randint(0, n-1)
    return board

def genetic(n, population_size = 100, generations = 1000, mutation_rate = 0.1):
    population = [init_board(n) for _ in range(population_size)]
    fitnesses = [fitness(board) for board in population]
    best = max(population, key=fitness)
    if h(best) == 0: return best, 1, 0, h(best)

    start = time.time()

    for i in range(generations):
        new_population = []
        for _ in range(population_size):
            parent_1 = select(population, fitnesses)
            parent_2 = select(population, fitnesses)
            child = crossover(parent_1, parent_2)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        best = max(new_population, key=fitness)
        if h(best) == 0: break

        new_population.sort(key=fitness, reverse=True)
        top_25 = new_population[:int(0.15 * population_size)]
        population = top_25 + [init_board(n) for _ in range(population_size - len(top_25))]  

    end = time.time()
    final_time = end - start


    return best, i + 1, final_time, h(best)

def genetic2(n, population_size = 100, generations = 1000, mutation_rate = 0.1):
    population = [init_board(n) for _ in range(population_size)]
    start = time.time()
    for generation in range(generations):
        fitnesses = [fitness(board) for board in population]
        new_population = []

        for _ in range(population_size):
            parent1 = select(population, fitnesses)
            parent2 = select(population, fitnesses)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population
        best_board = max(population, key=fitness)
        if h(best_board) == 0:
            break
    
    end = time.time()
    final_time = end - start
    return best_board, generation, final_time, h(best_board)

####

def hill_climbing_with_tracking(n, max_iterations=1000):
    current_board = init_board(n)
    current_conflicts = h(current_board)
    states_explored = 0
    start = time.time()
    h_values = []  # Lista para almacenar los valores de h(board)
    
    while states_explored < max_iterations:
        neighbors = get_neighbors(current_board)
        next_board = None
        next_conflicts = current_conflicts
        h_values.append(current_conflicts)  # Guardar el valor actual de h(board)
        
        for neighbor in neighbors:
            conflicts = h(neighbor)
            states_explored += 1
            if conflicts < next_conflicts:
                next_board = neighbor
                next_conflicts = conflicts
        
        if next_conflicts >= current_conflicts:
            break
        
        current_board = next_board
        current_conflicts = next_conflicts

    end = time.time()
    final_time = end - start

    return current_board, states_explored, final_time, current_conflicts, h_values

def simulated_annealing_with_tracking(n, max_iterations=1000):
    initial_temperature = 1000
    final_temperature = 1
    cooling_rate = 0.99  
    states_explored = 0

    current_board = init_board(n)
    h_values = []  # Lista para almacenar los valores de h(current_board)

    temperatures = np.arange(initial_temperature, final_temperature, -cooling_rate)
    
    start = time.time()

    for t in temperatures:
        temp = schedule(t)
        current_neighbors = get_neighbors(current_board)
        new_board = random.choice(current_neighbors)
        delta_e = h(new_board) - h(current_board)

        states_explored += 1
        if delta_e < 0 or random.random() < prob(delta_e, temp):
            current_board = new_board
        h_values.append(h(current_board))
        if h(current_board) == 0: break
        if states_explored >= max_iterations: break
    
    end = time.time()

    final_time = end - start

    return current_board, states_explored, final_time, h(current_board), h_values

def genetic_with_tracking(n, population_size=100, generations=1000, mutation_rate=0.1):
    population = [init_board(n) for _ in range(population_size)]
    fitnesses = [fitness(board) for board in population]
    best = max(population, key=fitness)
    h_values = [h(best)]  # Lista para almacenar los valores de h(best)
    if h(best) == 0: return best, 1, 0, h(best), h_values

    start = time.time()

    for i in range(generations):
        new_population = []
        for _ in range(population_size):
            parent_1 = select(population, fitnesses)
            parent_2 = select(population, fitnesses)
            child = crossover(parent_1, parent_2)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        best = max(new_population, key=fitness)
        h_values.append(h(best))  # Guardar el valor de h(best)
        if h(best) == 0: break

        new_population.sort(key=fitness, reverse=True)
        top_25 = new_population[:int(0.15 * population_size)]
        population = top_25 + [init_board(n) for _ in range(population_size - len(top_25))]  

    end = time.time()
    final_time = end - start

    return best, i + 1, final_time, h(best), h_values

def genetic2_with_tracking(n, population_size=100, generations=1000, mutation_rate=0.1):
    population = [init_board(n) for _ in range(population_size)]
    h_values = []  # Lista para almacenar los valores de h(best_board)
    start = time.time()
    for generation in range(generations):
        fitnesses = [fitness(board) for board in population]
        new_population = []

        for _ in range(population_size):
            parent1 = select(population, fitnesses)
            parent2 = select(population, fitnesses)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population
        best_board = max(population, key=fitness)
        h_values.append(h(best_board))  # Guardar el valor de h(best_board)
        if h(best_board) == 0:
            break
    
    end = time.time()
    final_time = end - start
    return best_board, generation, final_time, h(best_board), h_values