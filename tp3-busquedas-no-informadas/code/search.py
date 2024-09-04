from exploration import generate_random_map_custom
import gymnasium as gym
from gymnasium.envs.toy_text.frozen_lake import generate_random_map
from gymnasium import wrappers
from queue import PriorityQueue

def neighbors(position, desc):
    neighbors = []
    x, y = position
    if x > 0:
        neighbors.append((x - 1, y))
    if x < len(desc) - 1:
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < len(desc[0]) - 1:
        neighbors.append((x, y + 1))
    return neighbors

def bfs(desc, start):
    frontier = [(start, [])]
    explored = set()

    while frontier:

        position, path = frontier.pop(0)
        x, y = position

        if position in explored: continue

        explored.add(position)

        if desc[x][y] == "G":
            return path + [position], explored
        
        for n in neighbors(position, desc):
            if n not in explored and desc[n[0]][n[1]] != "H":
                frontier.append((n, path + [position]))
    return None, explored

def dfs(desc, start):
    frontier = [(start, [])]
    explored = set()

    while frontier:

        position, path = frontier.pop()
        x, y = position

        if position in explored: continue

        explored.add(position)

        if desc[x][y] == "G":
            return path + [position], explored
        
        for n in neighbors(position, desc):
            if n not in explored and desc[n[0]][n[1]] != "H":
                frontier.append((n, path + [position]))
    return None, explored

def dls(desc, start, limit):
    frontier = [(start, [], 0)]
    explored = set()

    while frontier:

        position, path, depth = frontier.pop()
        x, y = position

        if position in explored: continue

        explored.add(position)

        if desc[x][y] == "G": return path + [position], explored

        if depth > limit: continue
        
        for n in neighbors(position, desc):
            if n not in explored and desc[n[0]][n[1]] != "H":
                frontier.append((n, path + [position], depth + 1))
    return None, explored


env, desc = generate_random_map_custom(8, 0.3)
start_state = env.reset()[0]
for i in range(len(desc)):
    for j in range(len(desc[i])):
        if desc[i][j] == 'S':  
            start_position = (i, j)


print(bfs(desc, start_position))
print(dfs(desc, start_position))