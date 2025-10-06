import math

class Point3D(list):

    def __init__(self, x = 0, y = 0, z = 0):
        self.append(x)
        self.append(y)
        self.append(z)

    def norm2_sqr(self):
        result = 0
        for coord in self:
              result +=  coord*coord
        return result

    def norm2(self):
        return math.sqrt(self.norm2_sqr())

    def __add__(self, point2):
        result = Point3D()
        result[0] = self[0]+point2[0]
        result[1] = self[1]+point2[1]
        result[2] = self[2]+point2[2]
        return result

    def __sub__(self, point2):
        result = Point3D()
        for coord in range(len(self)):
            result[coord] = self[coord] - point2[coord]
        return result

    def __mul__(self, point2):
    
        if type(point2) == Point3D:
            result = Point3D()
            for coord in range(len(self)):
                result[coord] = self[coord] * point2[coord]
            return result

        if type(point2) == int or float:
            result = Point3D()
            for coord in range(len(self)):
                result[coord] = self[coord]*point2
            return result

    
    def __iadd__(self, point2):
        result = Point3D()
        for coord in range(len(self)):
            result[coord] = self[coord] * point2[coord]
        return result

    def __isub__(self, point2):
        result = Point3D()
        for coord in range(len(self)):
            result[coord] = self[coord] - point2[coord]
        return result

    def __imul__(self, point2):
        result = Point3D()
        for coord in range(len(self)):
            result[coord] = self[coord] * point2[coord]


    def normalize(self):
        nor = self.norm2()
        for coord in range(len(self)):
            self[coord] *= 1/nor
        return self

    def __str__(self):
        output = ""
        for coord in self:
            output += (str(coord)) + " "
        return output


def distance(point1, point2):
     return (point1-point2).norm2()

