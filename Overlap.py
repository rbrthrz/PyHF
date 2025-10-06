import numpy as np
from Basis import *
import math

class Overlap(np.ndarray): 

    def __new__(self, basis):
        self = np.zeros((len(basis), len(basis)))
        for i,func1 in enumerate(basis):
            for j,func2 in enumerate(basis):
               a, b = func1.exponent, func2.exponent 
               A, B = func1.center, func2.center     
               self[i][j] = pow((math.pi/(a+b)),1.5)*(math.exp( (-((a*b)/(a+b))) * (A-B).norm2_sqr()))
        return self

