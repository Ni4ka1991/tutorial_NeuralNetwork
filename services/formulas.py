#!/usr/bin/env python3

import numpy as np

# activation function

def sigmoid( var ):
    return (1 / (1 + np.exp( -var )))

# derivative of sigmoid

def deriv_sigmoid( v ):
    fv = sigmoid( v )        # use function def sigmoid()
    return fv * ( 1 - fv )   # return result of derivative of sigmoid resolved by formula


