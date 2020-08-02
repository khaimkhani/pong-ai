import random
from nn import *
from PayAI import *

class Genes:

    def __init__(self, population, mr):
        self.size = population
        self.initial_size = population
        self.popu = []
        self.old = []
        self.old_fit = []
        self.mutation_rate = mr
        for i in range(self.size):
            self.popu.append(PayAI())

    def offering(self):

        child = self.popu.pop(0)
        #self.old.append(child)
        #self.old_fit.append(child.fitness)
        self.size -= 1
        return child

    def pickBestFitnessInd(self):
        fitsum = sum(self.old_fit)
        ind = 0
        r = random.uniform(0, 1)
        while r > 0:
            r -= self.old_fit[ind] / fitsum
            ind += 1
        ind -= 1
        return ind

    def new_gen(self):

        n1 = self.old[self.pickBestFitnessInd()].brain
        n2 = self.old[self.pickBestFitnessInd()].brain

        self.old_fit.clear()
        self.old.clear()

        for i in range(self.initial_size):

            newthang = crossover(n1, n2)

            newthang.mutate(self.mutation_rate)
            thang = PayAI()
            thang.brain = newthang
            self.popu.append(thang)
        self.size = self.initial_size

def crossover(n1, n2):

    child = NeuralNetwork(n1.i, n1.h1, n1.h2, n1.o, n1.lr)
    layer_pointers_n1 = [n1.W_ih.copy(), n1.W_hh.copy(), n1.W_ho.copy()]
    layer_pointers_n2 = [n2.W_ih.copy(), n2.W_hh.copy(), n2.W_ho.copy()]
    swap = random.randint(1, 3)
    layer_pointers_n1[swap - 1] = layer_pointers_n2[swap - 1]
    child.W_ih = layer_pointers_n1[0]
    child.W_hh = layer_pointers_n1[1]
    child.W_ho = layer_pointers_n1[2]
    return child





