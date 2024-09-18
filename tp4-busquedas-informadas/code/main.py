import random
import gymnasium as gym #type: ignore
from search import *
import time
import pandas as pd
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt

def generate_random_map_custom(size, hprob):
    # Crear una matriz de tamaño 'size' x 'size' con caracteres "A"
    desc = [["A" for _ in range(size)] for _ in range(size)]
    agent_done = False
    end_done = False
    
    for i in range(size):
        for j in range(size):
            if random.random() < hprob:
                desc[i][j] = "H"
            else:
                desc[i][j] = "F"

    if not agent_done:
        agent_x = random.randint(0, size - 1)
        agent_y = random.randint(0, size - 1)
        desc[agent_x][agent_y] = "S"
        agent_done = True
    
    if not end_done:
        desc[size-1][size-1] = "G"
        end_done = True

    # Convertir cada sublista en una cadena
    for i in range(size):
        desc[i] = "".join(desc[i])
    
    env = gym.make('FrozenLake-v1', desc=desc, render_mode='human')
    return env, desc

def generate_envs(it):
    envs = []
    for _ in range(it):
        _, desc = generate_random_map_custom(8, 0.3)
        for i in range(len(desc)):
                for j in range(len(desc[i])):
                    if desc[i][j] == 'S':  
                        start_position = (i, j)
        for k in range(len(desc)):
                for l in range(len(desc[k])):
                    if desc[k][l] == 'G':  
                        goal = (k, l)
        envs.append((desc,start_position, goal))
    return envs


def run_experiments(it):
    results = []
    functions = [bfs, dfs, dls, ucs1, ucs2, rand, a_star]
    envs = generate_envs(it)

    for func in functions:
        for env in envs:
            desc = env[0]
            start_position = env[1]

            start = time.time()
            if func.__name__ != 'a_star':
                result = func(desc, start_position)
            else:
                result = func(desc, start_position, env[2])
            end = time.time()

            final_time = end - start

            if len(result) == 3:
                path, explored, total_cost = result
            elif len(result) == 2:
                path, explored = result
                total_cost = None
            
            states_n = len(explored)
            algorithm_name = func.__name__
            env_n = envs.index(env)
            cost_e1 = len(path) if path != None else 0

            if func.__name__ == "ucs1" or func.__name__ == "ucs2":
                cost_e2 = total_cost
            else: 
                cost_e2 = len(path) if path != None else 0

            solution_found = True if path != None else False

            results.append({
                'algorithm_name': algorithm_name,
                'env_n': env_n,
                'states_n': states_n,
                'cost_e1': cost_e1,
                'cost_e2': cost_e2,
                'time': final_time,
                'solution_found': solution_found
            })
    
    df = pd.DataFrame(results)
    df.to_csv('informada-results.csv', index=False)
    return df

def calculate_n_plot(df):
    mean_states_n = df['states_n'].mean()
    std_states_n = df['states_n'].std()

    mean_cost_e1 = df['cost_e1'].mean()
    std_cost_e1 = df['cost_e1'].std()
    mean_cost_e2 = df['cost_e2'].mean()
    std_cost_e2 = df['cost_e2'].std()

    mean_time = df['time'].mean()
    std_time = df['time'].std()

    # Crear un boxplot para cost_e1 por algorithm_name
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='algorithm_name', y='cost_e1', data=df)
    plt.title('Boxplot de cost_e1 por algorithm_name')
    plt.xlabel('Algorithm Name')
    plt.ylabel('Cost E1')

    # Guardar el boxplot como una imagen
    plt.tight_layout()
    plt.savefig('images/boxplot_cost_e1_por_algorithm_name.png')

    # Crear un boxplot para cost_e2 por algorithm_name
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='algorithm_name', y='cost_e2', data=df)
    plt.title('Boxplot de cost_e2 por algorithm_name')
    plt.xlabel('Algorithm Name')
    plt.ylabel('Cost E2')

    # Guardar el boxplot como una imagen
    plt.tight_layout()
    plt.savefig('images/boxplot_cost_e2_por_algorithm_name.png')

    # Crear un boxplot para cost_e2 por algorithm_name
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='algorithm_name', y='time', data=df)
    plt.title('Boxplot de time por algorithm_name')
    plt.xlabel('Algorithm Name')
    plt.ylabel('Time')

    # Guardar el boxplot como una imagen
    plt.tight_layout()
    plt.savefig('images/boxplot_time_por_algorithm_name.png')

df = run_experiments(30)
calculate_n_plot(df)

