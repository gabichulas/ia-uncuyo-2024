import numpy as np

class Environment:
    def __init__(self,sizeX,sizeY,dirt_rate):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.dirt_rate = dirt_rate
        self.matrix = self.make_it_dirty()

    def make_it_dirty(self):
        matrix = np.zeros(self.sizeX*self.sizeY, dtype=int)
        dirty_amount = int(self.sizeX * self.sizeY * self.dirt_rate)
        matrix[np.random.choice(self.sizeX*self.sizeY, dirty_amount, replace=False)] = 1
        matrix = matrix.reshape(self.sizeX,self.sizeY)
        return matrix
    
    def is_dirty(self,posX,posY):
        return self.matrix[posX,posY]
    
    def get_performance(self):
        return (int(self.sizeX * self.sizeY * self.dirt_rate) - np.count_nonzero(self.matrix))/int(self.sizeX * self.sizeY * self.dirt_rate)
    
    def accept_action(self,action,x,y):
        if action == "Arriba":
            if x + 1 > (self.sizeX - 1):
                return False
            else:
                return True
        elif action == "Abajo":
            if x - 1 < 0:
                return False
            else:
                return True
        elif action == "Derecha":
            if y + 1 > (self.sizeY - 1):
                return False
            else:
                return True
        elif action == "Izquierda":
            if y - 1 < 0:
                return False
            else:
                return True
        elif action == "Limpiar":
            if self.is_dirty(x, y) == 1:
                self.matrix[x,y] = 0
                return True
            else:
                return False
        else:
            return False

    def print_environment(self): print(self.matrix)

env = env = Environment(5, 5, 0, 0, 0.2, 0, 0)
env.print_environment()
