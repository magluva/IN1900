# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 22:04:45 2017

@author: Magnus
"""

import sys
import numpy as np

def one_6(n, N):
    throws = np.random.randint(1, 7, (N, n))
    success = throws == 6
    success = np.sum(success, axis=1)
    M = success >= 1
    M = np.sum(M, axis=0)
    return M/N

def compare(n, N):
    e = 11/36
    c = one_6(n, N)
    print("{0}{1:^30}{2}".format("Computed", "Exact", "Error"))
    print("--------------------------------------------------")
    print("{0:.10f}{1:^23.10f}{2:.10f}\n".format(c, e, abs(e-c)))
    print("{0} throws, {1:.0e} experiments\n".format(n, N))
    
if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
        N = int(sys.argv[2])
    except:
        print("Wrong type or missing args!\n"+
              "Usage: python one_6_ndice.py 'throws' 'experiments'")
        sys.exit(2)
        
    print("\nMonte Carlo Simulation:\n")
    compare(n, N)
    
# Terminal Output:
'''
Monte Carlo Simulation:

Computed            Exact             Error
--------------------------------------------------
0.3000000000     0.3055555556      0.0055555556

2 throws, 1e+01 experiments



Computed            Exact             Error
--------------------------------------------------
0.3130000000     0.3055555556      0.0074444444

2 throws, 1e+03 experiments



Computed            Exact             Error
--------------------------------------------------
0.3053200000     0.3055555556      0.0002355556

2 throws, 1e+06 experiments


Computed            Exact             Error
--------------------------------------------------
0.3055641000     0.3055555556      0.0000085444

2 throws, 1e+08 experiments
'''