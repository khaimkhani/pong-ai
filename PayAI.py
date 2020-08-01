from nn import *
import math


class PayAI:

    def __init__(self):
        self.brain = NeuralNetwork(6, 4, 4, 3, None)
        self.fitness = 0

    def think(self, info):
        outs = self.brain.query(info)
        ol = []
        for i in outs[0]:
            ol.append(i)
        actions = ['UP', 'DOWN', 'STAY']
        return actions[ol.index(max(ol))]

    def set_fitness(self, fit):
        self.fitness = fit



