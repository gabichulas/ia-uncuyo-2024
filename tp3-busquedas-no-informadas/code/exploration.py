import gymnasium as gym # type: ignore
from gymnasium.envs.toy_text.frozen_lake import generate_random_map # type: ignore
from gymnasium import wrappers # type: ignore
import random
import time



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

