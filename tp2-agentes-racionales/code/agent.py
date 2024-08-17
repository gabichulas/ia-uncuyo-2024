from environment import *
import numpy as np
from abc import ABC, abstractmethod

class Agent(ABC):
    def __init__(self, env):
        self.posX = np.random.randint(0,env.sizeX - 1)
        self.posY = np.random.randint(0,env.sizeY - 1)
        self.points = 0
        self.env = env
        self.lives = 1000

    def up(self):
        if self.env.accept_action("Arriba",self.posX,self.posY):
            self.posX += 1
    
    def down(self):
        if self.env.accept_action("Abajo",self.posX,self.posY):
            self.posX -= 1

    def right(self):
        if self.env.accept_action("Derecha",self.posX,self.posY):
            self.posY += 1
    def left(self):
        if self.env.accept_action("Izquierda",self.posX,self.posY):
            self.posY -= 1
    
    def clean(self):
        if self.env.accept_action("Limpiar",self.posX,self.posY):
            self.points += 1

    def idle(self):
        pass

    def die(self):
        return True if self.lives == 0 else False

    @abstractmethod
    def think(self):
        return