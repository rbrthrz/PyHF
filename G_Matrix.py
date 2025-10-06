import numpy as np
from Basis import *
from P_Matrix import *
import math

def F0(t):
    if t == 0.0:
        return 1.0
    else:
        return 0.5*math.sqrt(math.pi/t)*math.erf(math.sqrt(t))



def two_el_integrals(basis, _a, _b, _c, _d):
    
    a = basis[_a].exponent
    b = basis[_b].exponent
    c = basis[_c].exponent
    d = basis[_d].exponent

    distance = (basis[_a].center-basis[_b].center).norm2_sqr()

    distance_2 = (basis[_c].center-basis[_d].center).norm2_sqr()

    P = (basis[_a].center*a+basis[_b].center*b)*(1/(a+b))
    
    Q = (basis[_c].center*c+basis[_d].center*d)*(1/(c+d))

    distance_3 = (P-Q).norm2_sqr()
    

    result = 2*math.pow(math.pi, 5.0/2.0)/((a+b)*(c+d)*math.sqrt(a+b+c+d))*math.exp((-a*b/(a+b))*distance - (c*d/(c+d))*distance_2)*F0((a+b)*(c+d)/(a+b+c+d)*distance_3)
    return result


class G_Matrix(np.ndarray): 


    def __new__(self, P, basis):
        self = np.zeros((len(P), len(P)))
    

        for mu,row in enumerate(P):
            for nu,col in enumerate(P):
                for lambd,row in enumerate(P):
                    for sigma,col in enumerate(P):
                        
                         self[mu][nu] += P[lambd][sigma] * ((two_el_integrals(basis,mu,nu,sigma,lambd))-0.5 * two_el_integrals(basis,mu,lambd,sigma,nu))
                        

        return self

