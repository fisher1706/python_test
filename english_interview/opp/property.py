"""
Property Decorators
    Property decorators in Python provide a way to define attributes with getter, setter, and deleter methods,
    allowing for controlled access and validation of object attributes.
"""


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self._radius = value

    @radius.deleter
    def radius(self):
        del self._radius


if __name__ == "__main__":
    # Use
    c = Circle(5)
    print(c.radius)  # out: 5
    c.radius = 10
    print(c.radius)  # out: 10
    del c.radius
    print(c.radius)  # call AttributeError
