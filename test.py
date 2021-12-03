#!/usr/bin/env python3

import numpy as np


a = np.random.normal( size = 0)
print(f"size = 0 : {a}")
a = np.random.normal(size = 13)
print(f"size = 13: {a}")
a = np.random.normal( size = (2, 4) )
print(f"size = (2, 4): {a}")
a = np.random.normal()
print(f"size = empty: {a}")



