from GaussianFunction import *
from Point3D import *
from Molecule import *

class Basis(list):

    def __init__(self, molecule, exp_list):
        for atom in molecule:
                for exponent in exp_list:
                    self.append(GaussianFunction(atom.coord, exponent))


    def __str__(self):
        output = ""
        for function in self:
           output += str(function) + "\n"
        return output


