from Point3D import *


class GaussianFunction:

    def __init__(self, center, exponent):
        self.center = center
        self.exponent = exponent

    def __str__(self):
        return str(self.exponent) + ", " + str(self.center)


