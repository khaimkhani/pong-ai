from nn import *
import math


class PayAI:

    def __init__(self):
        self.brain = NeuralNetwork(6, 10, 10, 3, None)
        self.fitness = 0

    def think(self, info):
        outs = self.brain.query(info)
        if max(outs) == outs[0]:
            #go up
            return 'UP'

        elif max(outs) == outs[1]:
            return 'DOWN'
        else:
            return 'STAY'

    def set_fitness(self, time):
        self.fitness = math.ceil(time)



