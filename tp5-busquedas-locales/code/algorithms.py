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

def hill_climbing(n, max_iterations=1000):
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

def simulated_annealing(n, max_iterations=1000):
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

