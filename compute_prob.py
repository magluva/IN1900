# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 21:03:38 2017

@author: Magnus
"""

import numpy as np

def prob(N):
    picks = np.random.random(N)
    success = np.where(np.logical_and(picks>=0.5, picks<=0.6))
    M = np.shape(success)[1]
    return M/N

_exp = [1, 2, 3, 6]
N = np.asarray([10**i for i in _exp])
[print(prob(i)) for i in N]

# Terminal Output:
'''
0.0
0.09
0.11
0.100335
'''