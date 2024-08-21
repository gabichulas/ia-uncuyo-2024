from environment import *
import agent
import numpy as np
import random

class RefAgent(agent.Agent):
    def __init__(self, env):
        super().__init__(env)
    

    def think(self):
        trash_cell = self.verify_adj()
        if trash_cell:
            self.posX, self.posY = trash_cell
            self.clean()
            return

        #Si no limpia, se mueve a una casilla random

        moves = ["Arriba", "Abajo", "Izquierda", "Derecha"]
        move = random.choice(moves)
        if move == "Arriba":
            self.up()
        elif move == "Abajo":
            self.down()
        elif move == "Izquierda":
            self.left()
        elif move == "Derecha":
            self.right()

        self.idle()