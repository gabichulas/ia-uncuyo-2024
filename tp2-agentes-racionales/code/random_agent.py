from environment import *
import agent
import numpy as np
import random

class RandAgent(agent.Agent):
    def __init__(self, env):
        super().__init__(env)
    

    def think(self):
        moves = ["Arriba", "Abajo", "Izquierda", "Derecha"]
        move = random.choice(moves)
        if move == "Arriba":
            self.up()
            self.clean()
        elif move == "Abajo":
            self.down()
            self.clean()
        elif move == "Izquierda":
            self.left()
            self.clean()
        elif move == "Derecha":
            self.right()
            self.clean()