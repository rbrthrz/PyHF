import numpy as np
from Basis import *
import math

class P_Matrix(np.ndarray): 

    def __new__(self, C, molecule):
        self = np.zeros((len(C), len(C)))
        N = 0.0

        for atom in molecule:
            N += atom.nProtons

        N_half=N/2
    

        for i,row in enumerate(C):
            for j,col in enumerate(C):
                for a in range(int(N_half)):
                    self[i][j] += 2*(C[i,a]*C[j,a])


        return self

