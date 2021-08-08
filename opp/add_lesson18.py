# https://www.youtube.com/watch?v=xPsyicLd89g&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=18

import math

class Point2D:
    __slots__ = ('x', 'y', '__len')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.len = math.sqrt(x * x + y * y)

    @property
    def len(self):
        return self.__len

    @len.setter
    def len(self, value):
        self.__len = value

class Point3D(Point2D):
    # pass

    __slots__ = 'z'

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

        