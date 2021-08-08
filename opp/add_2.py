# https://www.youtube.com/watch?v=WP2sqI2BkeY&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=3&t=603s

class Coord_value:
    # def __init__(self, name):
    #     self.__name = name

    def __set_name__(self, owner, name):
        print(name)
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value

    # def __delete__(self, obj):
    #     del self.__value

class Point:
    # coordX = Coord_value('coordX')
    # coordY = Coord_value('coordY')

    coordX = Coord_value()
    coordY = Coord_value()

    def __init__(self, x=0, y=0):
        self.coordX = x
        self.coordY = y

pt = Point(1, 2)
pt.coordX = 5

print(pt.coordX, pt.coordY)







