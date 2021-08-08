# https://www.youtube.com/watch?v=WP2sqI2BkeY&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=3&t=603s

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __check_value(val):
        if isinstance(val, int) or isinstance(val, float):
            return True
        return False

    def __get_x(self):
        print('вызов __get_x')
        return self.__x

    def __set_x(self, x):
        if Point.__check_value(x):
            self.__x = x
        else:
            raise ValueError('Неверный формат')

    def __del_x(self):
        print('delete')
        del self.__x

    coorDx = property(__get_x, __set_x, __del_x)


pt = Point(1, 2)
pt.coorDx = 100
x = pt.coorDx
print(x)

del pt.coorDx

pt.coorDx = 50
x = pt.coorDx
print(x)


