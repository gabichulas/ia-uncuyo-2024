import pandas as pd
import matplotlib.pyplot as plt
import time

def run_experiments(n, num_runs=30):
    results = {
        'algorithm': [],
        'n': [],
        'solution_found': [],
        'execution_time': [],
        'states_visited': []
    }

    for _ in range(num_runs):
        # Backtracking
        solution_found, exec_time, states_visited = n_queens_backtracking(n)
        results['algorithm'].append('backtracking')
        results['n'].append(n)
        results['solution_found'].append(solution_found)
        results['execution_time'].append(exec_time)
        results['states_visited'].append(states_visited)

        # Forward Checking
        solution_found, exec_time, states_visited = n_queens_forward_checking(n)
        results['algorithm'].append('forward_checking')
        results['n'].append(n)
        results['solution_found'].append(solution_found)
        results['execution_time'].append(exec_time)
        results['states_visited'].append(states_visited)

    return results

def main():
    results_4 = run_experiments(4)
    results_8 = run_experiments(8)
    results_10 = run_experiments(10)

    all_results = {key: results_4[key] + results_8[key] + results_10[key] for key in results_4}

    df = pd.DataFrame(all_results)
    df.to_csv(r'tp6-csp\n_queens_results.csv', index=False)

    stats = df.groupby(['algorithm', 'n']).agg(
        solution_rate=('solution_found', 'mean'),
        avg_time=('execution_time', 'mean'),
        std_time=('execution_time', 'std'),
        avg_states=('states_visited', 'mean'),
        std_states=('states_visited', 'std')
    ).reset_index()

    print(stats)

    plt.figure(figsize=(30, 15))
    df.boxplot(column='execution_time', by=['algorithm', 'n'], rot=45)
    plt.title('Distribución de Tiempos de Ejecución')
    plt.suptitle('')
    plt.xlabel('Algoritmo y N')
    plt.ylabel('Tiempo de Ejecución (s)')
    plt.tight_layout()
    plt.savefig(r'tp6-csp\images\exec_time_boxplot.png')
    plt.close()

    plt.figure(figsize=(30, 15))
    df.boxplot(column='states_visited', by=['algorithm', 'n'], rot=45)
    plt.title('Distribución de Estados Visitados')
    plt.suptitle('')
    plt.xlabel('Algoritmo y N')
    plt.ylabel('Estados Visitados')
    plt.tight_layout()
    plt.savefig(r'tp6-csp\images\states_boxplot.png')
    plt.close()

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i] == j:
            return False
    return True

def solve_n_queens_backtracking(board, row, n, states):
    if row == n:
        return True
    for col in range(n):
        states[0] += 1  
        if is_safe(board, row, col, n):
            board[row] = col
            if solve_n_queens_backtracking(board, row + 1, n, states):
                return True
            board[row] = -1
    return False

def n_queens_backtracking(n):
    board = [-1] * n
    states = [0]
    start_time = time.time()
    solution_found = solve_n_queens_backtracking(board, 0, n, states)
    end_time = time.time()
    return solution_found, end_time - start_time, states[0]

def is_safe_forward(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def forward_checking(board, row, n, domains, states):
    if row == n:
        return True
    for col in domains[row]:
        states[0] += 1  
        if is_safe_forward(board, row, col, n):
            board[row] = col
            new_domains = [list(domain) for domain in domains]
            for i in range(row + 1, n):
                if col in new_domains[i]:
                    new_domains[i].remove(col)
                if col - (i - row) in new_domains[i]:
                    new_domains[i].remove(col - (i - row))
                if col + (i - row) in new_domains[i]:
                    new_domains[i].remove(col + (i - row))
            if forward_checking(board, row + 1, n, new_domains, states):
                return True
            board[row] = -1
    return False

def n_queens_forward_checking(n):
    board = [-1] * n
    domains = [list(range(n)) for _ in range(n)]
    states = [0]
    start_time = time.time()
    solution_found = forward_checking(board, 0, n, domains, states)
    end_time = time.time()
    return solution_found, end_time - start_time, states[0]
    
main()