import numpy as np

class Environment:
    def __init__(self,sizeX,sizeY,dirt_rate,seed):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.dirt_rate = dirt_rate
        self.seed = seed
        self.matrix = self.make_it_dirty()

    def make_it_dirty(self):
        np.random.seed(self.seed)
        matrix = np.zeros(self.sizeX*self.sizeY, dtype=int)
        dirty_amount = int(self.sizeX * self.sizeY * self.dirt_rate)
        matrix[np.random.choice(self.sizeX*self.sizeY, dirty_amount, replace=False)] = 1
        matrix = matrix.reshape(self.sizeX,self.sizeY)
        return matrix
    
    def is_dirty(self, posX, posY):
        if 0 <= posX < self.sizeX and 0 <= posY < self.sizeY:
            return self.matrix[posX, posY]
        return False
    
    def get_performance(self):
        return ((self.sizeX * self.sizeY * self.dirt_rate) - np.count_nonzero(self.matrix))/(self.sizeX * self.sizeY * self.dirt_rate)
    
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

