"""
Inheritance
    Inheritance allows a class to inherit attributes and methods from another class, promoting code reuse and creating a
    hierarchical relationship between classes.

    super() - call to parent class - call first - without self

Overriding
    Subclasses can override methods from their superclasses to provide custom behavior while still inheriting
    and reusing code from the parent class.

Overloading
    Abstract base classes define a common interface that must be implemented by concrete subclasses.
    They provide a way to enforce contracts and ensure consistent behavior across related classes.
"""


class Geom:
    name = "Geom"

    def __init__(self, x1, y1, x2, y2):
        print(f"__init__ from GEOM for {self.__class__}")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    @staticmethod
    def draw():
        print("draw line")


class RectOne(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        print("---start---")
        super().__init__(x1, y1, x2, y2)
        print(f"__init__ from REACT for {self.__class__}")
        self.fill = fill

    @staticmethod
    def draw():
        print("draw React")


class Car:
    @staticmethod
    def start(a, b=None):
        if b is not None:
            print(a + b)
        else:
            print(a)



if __name__ == "__main__":
    line = Line(0, 0, 10, 20)
    print(line.__dict__)
    print(line.name)
    print("*" * 200)

    react = RectOne(1, 2, 3, 4)
    print(react.__dict__)
