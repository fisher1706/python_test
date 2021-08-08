# https://www.youtube.com/watch?v=WP2sqI2BkeY&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=3&t=603s

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def coorDx(self):
        return self.__x

    def __check_value(val):
        if isinstance(val, int) or isinstance(val, float):
            return True
        return False

    @coorDx.getter
    def coorDx(self):
        print('вызов __get_x')
        return self.__x

    @coorDx.setter
    def coorDx(self, x):
        if Point.__check_value(x):
            self.__x = x
        else:
            raise ValueError('Неверный формат')

    @coorDx.deleter
    def coorDx(self):
        print('delete')
        del self.__x


pt = Point(1, 2)
pt.coorDx = 100
x = pt.coorDx
print(x)

del pt.coorDx

pt.coorDx = 50
x = pt.coorDx
print(x)


