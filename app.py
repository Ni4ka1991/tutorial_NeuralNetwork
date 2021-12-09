#!/usr/bin/env python3

import numpy as np
from services.mean_squared_error import *
from services.formulas import *


# one artificial neuron properties
class Neuron:
    def __init__ ( self, weights, bias ):
        self.weights = weights
        self.bias = bias

    def feedforward( self, inputs ):
        total = np.dot( self.weights, inputs ) + self.bias
        return sigmoid( total )

############################

class OurNeuralNetwork:
    def __init__(self):
        ### Weights
        self.w1 = np.random.normal() #create an array that contains normally distributed ( Gaussian ) data ( in this case contains one element )
        self.w2 = np.random.normal()
        self.w3 = np.random.normal()
        self.w4 = np.random.normal()
        self.w5 = np.random.normal()
        self.w6 = np.random.normal()

        ### Biases
        self.b1 = np.random.normal()
        self.b2 = np.random.normal()
        self.b3 = np.random.normal()
        

    def feed_Forward( self, x ):
        h1 = sigmoid( self.w1 * x[0] + self.w2 * x[1] + self.b1 )  #first neuron 
        h2 = sigmoid( self.w3 * x[0] + self.w4 * x[1] + self.b2 )  #second neuron 
        o1 = sigmoid( self.w5 * h1 + self.w6 * h2 + self.b3 )      #output neuron 
        return o1


    def train( self, data, all_y_tryes ):
        lern_rate = 0.1
        epochs = 1000
        for epoch in range( epochs ):
            sum_h1 = self.w1 * x[0] + self.w2 * x[1] + self.b1
            h1 = sigmoid( sum_h1 )

            sum_h2 = self.w3 * x[0] + self.w4 * x[1] + self.b2
            h2 = sigmoid( sum_h2 )

            sum_o1 = self.w5 * h1 + self.w6 * h2 + self.b3
            o1 = sigmoid( sum_o1 )
            y_pred = o1

            d_L_d_ypred = -2 * ( y_true - y_pred )




network = OurNeuralNetwork()
x = np.array( [ 2, 3 ] )          #create an one-dimentional array of inputs x1 = 2, x2 = 3


print( network.feed_Forward( x ))
print( mse_loss(y_true, y_pred) )
