import numpy as np
import scipy as sp
import scipy.linalg
from Basis import *
from Molecule import *
from Overlap import *
from P_Matrix import *
from G_Matrix import *
from T_Matrix import *
from V_Matrix import *



class SCF:

    def __init__(self, xyz_file_location, max_iterations=250, exp_list =[1, 2], convergence_limit=0.0001): 

        molecule = Molecule(xyz_file_location)
        basis = Basis(molecule, exp_list)

        S = Overlap(basis)
        T = T_Matrix(basis)
        V = V_Matrix(basis, molecule)
        H_core = T + V


        X = sp.linalg.fractional_matrix_power(S, -0.5)
        
       
        P = np.zeros((len(basis), len(basis)))
        
        for a in range(max_iterations):

            G = G_Matrix(P, basis)
            X_dagger = X.transpose()
            F = H_core + G
            F_prime = np.matmul(np.matmul(X_dagger, F), X)
            Epsilon, C_prime = np.linalg.eig(F_prime)
            C_new = np.matmul(X, C_prime)
            P_old = P
            P = P_Matrix(C_new, molecule)

            if np.linalg.norm(P_old-P) < convergence_limit:
                print("Success!", "Norm=", np.linalg.norm(P_old-P))
                orb_energy, ev = np.linalg.eig(F_prime)
                print("Orbital Energies = \n", orb_energy)
                
                EHF_pre = 0
                for i,mu in enumerate(basis):
                    for j,nu in enumerate(basis):
                        EHF_pre += 0.5*(P[i][j]*(H_core[i][j] + F[i][j]))
                EHF = EHF_pre + molecule.nuclearPotential()
               
                print("EHF_pre=", EHF_pre, "nucPot=", molecule.nuclearPotential())

                print("EHF = ", EHF)


                break
        



if __name__ == "__main__":


    scf_test = SCF("H2.xyz", 1000, [0.3])
