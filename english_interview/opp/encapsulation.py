"""
Encapsulation
    Encapsulation is the mechanism of hiding data implementation details and restricting access to object's
    internal state. It promotes data abstraction and code modularity.

    atr - public - access for all
    _atr - protected - access from class and child classes
    __atr - private - access only from class
"""


class Point:
    def __init__(self, x, y):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, val):
        return type(val) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("coords must be digital")

    def get_coord(self):
        return self.__x, self.__y


if __name__ == "__main__":
    pt = Point(1, 2)
    pt.set_coord(10, 20)

    print(pt.get_coord())

    print(dir(pt))
    print(pt.__dict__)
    print(pt._Point__x)
