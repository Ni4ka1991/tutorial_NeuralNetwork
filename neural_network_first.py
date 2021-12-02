#!/usr/bin/env python3

import numpy as np


# activation function

def sigmoid( var ):
    return (1 / (1 + np.exp( -var )))
#


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
    def __init__( self ):
        weights = np.array( [ 0, 1 ] )
        bias = 0
        
        ### create a three AN with weights: 1 and 2 and bias=0
        self.h1 = Neuron( weights, bias )  # create a AN h1 with two weights w1=0, w2=1 and bias=0
        self.h2 = Neuron( weights, bias )
        self.o1 = Neuron( weights, bias )
        ########i

    def feed_Forward( self, x ):
        out_h1 = self.h1.feedforward( x )
        out_h2 = self.h2.feedforward( x )
        out_o1 = self.o1.feedforward( np.array( [ out_h1, out_h2 ] ))
        return out_o1



network = OurNeuralNetwork()
x = np.array( [ 2, 3 ] )          #create an one-dimentional array of inputs x1 = 2, x2 = 3

print( network.feed_Forward( x ))

