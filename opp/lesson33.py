class Rectangle:
    __slots__ = 'width', 'height'

    def __init__(self, a, b):
        self.width = a
        self.height = b

    @property
    def perimetr(self):
        return (self.width + self.height) * 2

    @property
    def area(self):
        return self.width * self.height


