import gymnasium as gym
from gymnasium.envs.toy_text.frozen_lake import generate_random_map
from gymnasium import wrappers
import random
import time

nuevo_limite = 3
env = gym.make('FrozenLake-v1', render_mode='human')
env = wrappers.TimeLimit(env, nuevo_limite)

print("Numero de estados:", env.observation_space.n)
print("Numero de acciones:", env.action_space.n)

state = env.reset()
print("Posici´on inicial del agente:", state[0])
done = truncated = False
while not (done or truncated):
    action = env.action_space.sample() # Acci´on aleatoria
    print(type(action))
    next_state, reward, done, truncated, _ = env.step(action)
    print(f"Acci´on: {action}, Nuevo estado: {next_state}, Recompensa: {reward}")
    print(f"¿Gan´o? (encontr´o el objetivo): {done}")
    print(f"¿Fren´o? (alcanz´o el m´aximo de pasos posible): {truncated}\n")
    state = next_state

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
    return env

