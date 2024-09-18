from queue import PriorityQueue
import random

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

def neighborsWithCost(position, desc):
    neighbors = []
    costList = []
    x, y = position
    if x > 0:
        neighbors.append((x - 1, y))
        costList.append(1)
    if x < len(desc) - 1:
        neighbors.append((x + 1, y))
        costList.append(3)
    if y > 0:
        neighbors.append((x, y - 1))
        costList.append(2)
    if y < len(desc[0]) - 1:
        neighbors.append((x, y + 1))
        costList.append(4)
    return neighbors, costList


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

def dls(desc, start):
    limit = 10
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

def ucs1(desc, start):
    frontier = PriorityQueue()
    frontier.put((0, start, []))
    explored = set()
    
    while not frontier.empty():
        cost, position, path = frontier.get()
        if position in explored: continue

        explored.add(position)

        x, y = position
        if desc[x][y] == "G": return path + [position], explored, cost

        for n in neighbors(position, desc):
            if n not in explored and desc[n[0]][n[1]] != "H":
                frontier.put((cost + 1, n, path + [position]))
    return None, explored, 0

def ucs2(desc, start):
    frontier = PriorityQueue()
    frontier.put((0, start, []))
    explored = set()
    accCost = {}
    accCost[start] = 0
    
    while not frontier.empty():
        cost, position, path = frontier.get()
        if position in explored: continue

        explored.add(position)

        x, y = position
        if desc[x][y] == "G": return path + [position], explored, cost

        neigh, costList = neighborsWithCost(position, desc)

        for n, costA in zip(neigh, costList):
            newCost = costA + cost
            if (n not in explored or newCost < accCost.get(n, float('inf'))) and desc[n[0]][n[1]] != "H":
                accCost[n] = newCost
                frontier.put((newCost, n, path + [position]))
    return None, explored, 0

def rand(desc, start):
    lifes = 100
    current_position = start
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    path = [current_position]
    explored = set()
    explored.add(current_position)
    
    while lifes > 0:
        move = random.choice(directions)
        new_position = (current_position[0] + move[0], current_position[1] + move[1])
        
        if 0 <= new_position[0] < len(desc) and 0 <= new_position[1] < len(desc[0]):
            current_position = new_position
            path.append(current_position)
            explored.add(current_position)
            
            if desc[current_position[0]][current_position[1]] == 'G':
                return path, explored
        
        lifes -= 1
    
    return None, explored

def h(n, goal): return abs(n[0] - goal[0]) + abs(n[1] - goal[1]) # Heuristica: Distancia Manhattan

def a_star(desc, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start, [start], 0))  # (priority, current_node, path, cost)
    explored = set()
    accCost = {start: 0}

    while not frontier.empty():
        _, current, path, current_cost = frontier.get()
        
        if current == goal: return path, explored, current_cost
        
        if current in explored: continue
        
        explored.add(current)
        
        neighbors, costs = neighborsWithCost(current, desc)

        for neighbor, cost in zip(neighbors, costs):
            new_cost = current_cost + cost
            if (neighbor not in explored or new_cost < accCost.get(neighbor, float('inf'))) and desc[neighbor[0]][neighbor[1]] != "H":
                accCost[neighbor] = new_cost
                priority = new_cost + h(neighbor, goal)
                frontier.put((priority, neighbor, path + [neighbor], new_cost))

    return None, explored, 0