class Point2D:
    __slots__ = ('x', 'y', '__length')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = (x * x + y * y) ** 0.5

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value


if __name__ == '__main__':
    pt = Point2D(1, 2)
    print(pt.length)

    pt.length = 10
    print(pt.length)
    