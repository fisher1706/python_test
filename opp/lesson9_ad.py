# https://www.youtube.com/watch?v=WP2sqI2BkeY&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=3&t=603s

class Point:
    WIDTH = 5

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __check_value(val):
        if isinstance(val, int) or isinstance(val, float):
            return True
        return False

    def set(self, x, y):
        if Point.__check_value(x) and Point.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            print('bad')

    def get(self):
        return self.__x, self.__y

    def __getattribute__(self, item):
        if item == '_Point__x':
            return '__variable'
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'WIDTH':
            raise AttributeError
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        print('__getattr__: ' + item)

    def __delattr__(self, item):
        print('__delattr__: ' + item)

pt = Point(1, 2)
print(pt.get())
pt.set(10, 20)
print(pt.get())

pt._Point__y = 50

print(pt._Point__y)
print(pt._Point__x)

# pt.WIDTH = 10

print(pt.WIDTH)

pt.zzz
