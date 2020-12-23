# Problem 1
# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

import math


class Line:

    def __init__(self, coor1, coor2):
        self.x1 = coor1[0]
        self.y1 = coor1[1]
        self.x2 = coor2[0]
        self.y2 = coor2[1]

    def distance(self):
        return math.sqrt(math.pow(self.x2 - self.x1, 2)
                         + math.pow(self.y2 - self.y1, 2))

    def slope(self):
        return (self.y2 - self.y1) / (self.x2 - self.x1)

#  Calculate Cylinder parameters
class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi * math.pow(self.radius, 2) * self.height

    # 2(pi)radius(height) + 2(pi)radius squared. 2πrh+2πr2
    def surface_area(self):
        return (2 * math.pi * self.radius * self.height) + (2 * math.pi * math.pow(self.radius, 2))



if __name__ == '__main__':
    coordinate1 = (3, 2)
    coordinate2 = (8, 10)
    li = Line(coordinate1, coordinate2)
    li.distance()
    # li.slope()
