from Point3D import *
from Atom import *
import math

class Molecule(list):
    

    def __init__(self, xyz_file_name):
        with open(xyz_file_name, "r") as xyz_file:
            nAtoms = int(xyz_file.readline())
            xyz_file.readline()
            lines = xyz_file.readlines()
            for line in lines:
                name, x , y , z = line.split()
                location = Point3D(float(x), float(y), float(z))
                self.append(Atom(name, location))

    def __str__(self):
        output = ""
        for atom in range(len(self)):
            output += str(self[atom]) + "\n"
        return output


    def nuclearPotential(self):
        Pot = 0
        for i in range(len(self)):
            for j in range(i+1, len(self)):
               Pot += (self[i].nProtons*self[j].nProtons)/(distance(self[i].coord, self[j].coord)) 
        return Pot


