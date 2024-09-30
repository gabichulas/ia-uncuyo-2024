import random
import time

def init_board(n):
    return [random.randint(0, n-1) for _ in range(n)]

def calculate_conflicts(board):
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

def hill_climbing(n, max_iterations=1000):
    current_board = init_board(n)
    current_conflicts = calculate_conflicts(current_board)
    states_explored = 0
    start = time.time()
    
    while states_explored < max_iterations:
        neighbors = get_neighbors(current_board)
        next_board = None
        next_conflicts = current_conflicts
        
        for neighbor in neighbors:
            conflicts = calculate_conflicts(neighbor)
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


n = 8
max_iterations = 1000
solution, states_explored, elapsed_time, conflicts = hill_climbing(n, max_iterations)
print(f"Solución: {solution}")
print(f"Estados explorados: {states_explored}")
print(f"Tiempo transcurrido: {elapsed_time} segundos")
print(f"Conflictos: {conflicts}")