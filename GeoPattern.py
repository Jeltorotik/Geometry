from math import sqrt, acos, pi, atan2, atan
from decimal import *
getcontext().prec = 40

class Vector:
    #Ininitalization
    def __init__(self, coords=[]):
        self.coords = coords
        
    #print()
    def __str__(self):
        return ' '.join(map(str, self.coords))

    #How many dimensions, e.g [x, y, z, ...]
    def dim(self):
        return len(self.coords)

    # distanse between point and basis of coordinates
    def length(self):
        return sqrt(sum([i*i for i in self.coords]))

    #Normalization of vector
    def norm(self):
        length_temp = Vector.length(self)
        return Vector([i/length_temp for i in self.coords])

    # Whether vectors are equal
    def __eq__(self, other):
        for i, j in zip(self.coords, other.coords):
            if i != j:
                return False
        return True

    # Sum of vectors
    def __add__(self, other):
        try:
            return Vector([i + other for i in self.coords])
        except:
            return Vector([i + j for i, j in zip(self.coords, other.coords)])
    #Difference of vectors
    def __sub__(self, other):
        try:
            return Vector([i - other for i in self.coords])
        except:
            return Vector([i - j for i, j in zip(self.coords, other.coords)])

    def __mul__(self, other):
        try:
            return Vector([i * other for i in self.coords])
        except:
            # dot product
            return sum([i * j for i, j in zip(self.coords, other.coords)])

    def __truediv__(self, other):
        return Vector([i / other for i in self.coords])

    # Cross product (only for 2 dimensional)
    def __xor__(self, other):
        return self.coords[0] * other.coords[1] - self.coords[1] * other.coords[0]
    
    #Distance between vectors 
    def dist(self, other):
        return sqrt(sum([(i-j)**2 for i, j in zip(self.coords, other.coords)]))
    
    def __abs__(self):
        return Vector([abs(i) for i in self.coords])
    
    def __pow__(self, other):
        return Vector([i**other for i in self.coords])


def angle(v1, v2, between = Vector([0, 0]), oriented = True, degrees = False):
    
    alpha = atan2(*(v1 - between).coords[::-1])
    beta = atan2(*(v2 - between).coords[::-1])
    if not oriented:
        gamma = abs(alpha - beta)
    else:
        gamma = alpha - beta
   

    #Normalization
    while gamma >= 2 * pi - eps:
        gamma -= 2 * pi
    while gamma <= -2 * pi + eps:
        gamma += 2*pi
        
    if not oriented:
        if gamma > pi - eps:
            gamma = 2*pi - gamma
    else:
        if gamma < -eps:
            gamma = 2*pi + gamma
            
    if degrees:
        gamma = gamma/pi * 180
            
    return gamma

# Equation of straight line
def esl(a, b, c):
    # Ax + By + C = 0
    # (y1 - y2)x + (x2 - x1)y + (x1y2 - x2y1) = 0
    straight = (a[1] - b[1]) * c[0] + (b[0] - a[0]) * c[1] + (a[0]*b[1] - a[1]*b[0])
    return straight

def isintersect(p = []):
    if p[0] > p[1]:
        p[0], p[1] = p[1], p[0]
    if p[2] > p[3]:
        p[2], p[3] = p[3], p[2]
    return max(p[0], p[2]) <= min(p[1], p[3])

class Polygon:
    def __init__(self, vectors=[]):
        self.vectors = vectors

    def area(self):
        result = 0
        self.vectors.append(self.vectors[0])
        for i in range(len(self.vectors) - 1):
            result += self.vectors[i] ^ self.vectors[i + 1]
        self.vectors.pop()
        return abs(result) / 2.0

eps = 1e-10


'''
#Input
filein = open('input.in', 'r')
data = list(map(float, filein.read().split()))
filein.close()
#Output
out = '1'
fileout = open('output.out', 'w')
fileout.write(out)
fileout.close()
'''
