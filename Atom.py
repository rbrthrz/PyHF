from Point3D import *
import math

periodic_table = {"H":1, "He":2, "Li":3, "Be":4, "B":5, "C":6, "N":7, "O":8}



class Atom:

    def __init__(self, name, coord):
        self.name = name
        self.coord = coord
        self.nProtons = periodic_table[name]
        
    

    def __str__(self):
        return self.name + ", " + str(self.nProtons) + ", "  + str(self.coord)



