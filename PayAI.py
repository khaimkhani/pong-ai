from nn import *
import math


class PayAI:

    def __init__(self):
        self.brain = NeuralNetwork(4, 3, 3, 3, None)
        self.fitness = 0

    def think(self, info):
        outs = self.brain.query(info)
        ol = outs.flatten()
        if max(ol) == ol[0]:
            return 'UP'
        elif max(ol) == ol[1]:
            return 'DOWN'
        else:
            return 'STAY'


    def set_fitness(self, fit):
        self.fitness = fit



