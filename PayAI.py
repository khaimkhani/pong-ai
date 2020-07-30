from nn import *
import math


class PayAI:

    def __init__(self):
        self.brain = NeuralNetwork(6, 4, 4, 3, None)
        self.fitness = 0

    def think(self, info):
        outs = self.brain.query(info)
        num = random.uniform(0, 1)
        if num <= outs[0]:
            #go up
            return 'UP'

        elif outs[0] < num <= outs[0] + outs[1]:
            return 'DOWN'
        else:
            return 'STAY'

    def set_fitness(self, fit):
        self.fitness = fit



