import numpy
import scipy.special
import pygame
import random


class NeuralNetwork:
    """
    Neural network class. thats it. thats the class. oh and also it has a bias node built in at input and hidden layers.
    and also two hidden layers for complex learning wowow.
    god bless.
    """

    def __init__(self, inp, hid1, hid2, out, lr):
        """
        Initiate NN object
        :param inp:
        :type inp:
        :param hid:
        :type hid:
        :param out:
        :type out:
        :param lr:
        :type lr:
        """
        self.bias = 1
        self.i = inp
        self.h1 = hid1
        self.h2 = hid2
        self.o = out
        self.lr = lr
        self.W_ih = numpy.random.normal(0, pow(self.h1, -.5), (self.h1, self.i + 1))
        self.W_hh = numpy.random.normal(0, pow(self.h2, -.5), (self.h2, self.h1 + 1))
        self.W_ho = numpy.random.normal(0, pow(self.o, -.5), (self.o, self.h2 + 1))

    def train(self, inputs, targets):
        ins = inputs.copy()
        ins = self.norm_ins(ins)
        ins.append(self.bias)
        target = numpy.array(targets, ndmin=2).T
        ins = numpy.array(ins, ndmin=2).T
        h1_ins = numpy.dot(self.W_ih, ins)

        h1_outs_nb = self.activation(h1_ins) #activation of hidden layer 1 with no bias node obviously duhhh.

        h1_outs = numpy.insert(h1_outs_nb, h1_outs_nb.size, 1, 0) #activation of hidden layer 2

        h2_ins = numpy.dot(self.W_hh, h1_outs)

        h2_outs_nb = self.activation(h2_ins)

        h2_outs = numpy.insert(h2_outs_nb, h2_outs_nb.size, 1, 0)

        final_outs_in = numpy.dot(self.W_ho, h2_outs)
        final_out = self.activation(final_outs_in)
        error = target - final_out

        hidden2_errors = numpy.dot(self.W_ho.T, error)
        backprop_errorH2 = numpy.delete(hidden2_errors, -1, 0) #removing bias errors so they dont get sent back to input
        hidden1_errors = numpy.dot(self.W_hh.T, backprop_errorH2)
        backprop_errorH1 = numpy.delete(hidden1_errors, -1, 0) #removing bias errors
        self.W_ho += self.lr * numpy.dot((error * final_out * (1 - final_out)), numpy.transpose(numpy.insert(h1_ins, h1_ins.size, 1, 0)))
        self.W_hh += self.lr * numpy.dot((backprop_errorH2 * h2_outs_nb * (1 - h2_outs_nb)), numpy.transpose(numpy.insert(h2_ins, h2_ins.size, 1, 0)))
        self.W_ih += self.lr * numpy.dot((backprop_errorH1 * h1_outs_nb * (1 - h1_outs_nb)), numpy.transpose(inputs))




    def query(self, inputs_list):

        ins = inputs_list.copy()
        ins = self.norm_ins(ins)
        ins.append(self.bias)
        ins = numpy.array(ins, ndmin=2).T
        hidden1_inputs = numpy.dot(self.W_ih, ins)
        hidden1_outputs = self.activation(hidden1_inputs)
        hidden1_outputs = numpy.insert(hidden1_outputs, hidden1_outputs.size, 1, 0)
        hidden2_inputs = numpy.dot(self.W_hh, hidden1_outputs)
        hidden2_outputs = self.activation(hidden2_inputs)
        hidden2_outputs = numpy.insert(hidden2_outputs, hidden2_outputs.size, 1, 0)
        output_inputs = numpy.dot(self.W_ho, hidden2_outputs)
        outputs = self.activation(output_inputs)
        return self.norm_outs(outputs)

    def norm_outs(self, outs):
        for i in range(len(outs)):
            outs[i] = outs[i] / sum(outs)
        return outs

    def norm_ins(self, ins):
        for i in range(len(ins)):
            ins[i] = ins[i] / sum(ins)
        return ins

    def activation(self, x):
        return scipy.special.expit(x)

    def mutate(self, rate):

        for i in self.W_ih:
            for j in i:
                if random.uniform(0, 1) < rate:
                    self.W_ih[i][j] = random.uniform(-1, 1)
        for i in self.W_hh:
            for j in i:
                if random.uniform(0, 1) < rate:
                    self.W_ih[i][j] = random.uniform(-1, 1)
        for i in self.W_ho:
            for j in i:
                if random.uniform(0, 1) < rate:
                    self.W_ih[i][j] = random.uniform(-1, 1)



if __name__ == "__main__":
    x = NeuralNetwork(2, 3, 3, 2, 0.5)
    x.train([1,0], [1, 0])




