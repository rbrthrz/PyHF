import numpy as np
from Basis import *
from Molecule import *
from Point3D import *
import math

def F0(t):
    if t == 0.0:
        return 1.0
    else:
        return 0.5*math.sqrt(math.pi/t)*math.erf(math.sqrt(t))

class V_Matrix(np.ndarray): 

    def __new__(self, basis, molecule):
        self = np.zeros((len(basis), len(basis)))
        for i,func1 in enumerate(basis):
            for j,func2 in enumerate(basis):
                for k,atom in enumerate(molecule):
                    a, b = func1.exponent, func2.exponent 
                    A, B = func1.center, func2.center
                    C = atom.coord
                    z = atom.nProtons
                    distance = (A-B).norm2_sqr()
                    P = ((A*a+B*b)*(1/(a+b)))
                    distance2 = (P-C).norm2_sqr()

                    self[i][j] += -(2*math.pi)/(a+b)*z*math.exp(((-a*b)/(a+b))*distance )*F0((a+b)*distance2)


        return self

