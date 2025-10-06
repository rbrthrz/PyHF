import numpy as np
from Basis import *
import math

class T_Matrix(np.ndarray): 

    def __new__(self, basis):
        self = np.zeros((len(basis), len(basis)))
        for i,func1 in enumerate(basis):
            for j,func2 in enumerate(basis):
               a, b = func1.exponent, func2.exponent 
               A, B = func1.center, func2.center     
               
               R_square = (basis[i].center - basis[j].center).norm2_sqr() 
               self[i][j] = ( (a*b)/(a+b) ) * ( 3 - ( ((2*a*b) / (a+b) ) * R_square ) ) * ( math.pow((math.pi/(a+b)),1.5) ) * math.exp( -((a*b)/(a+b))*R_square )


            #   pow((math.pi/(a+b)),1.5)*(math.exp( (-((a*b)/(a+b))) * (A-B).norm2_sqr()))
        return self

