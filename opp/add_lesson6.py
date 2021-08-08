# https://www.youtube.com/watch?v=VQ6vUzqAInU&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=6

class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __str__(self):
        return f'{self._x}, {self._y}'

class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        print('__init__ Prop')
        self._sp = sp
        self._ep = ep
        self._color = color
        self.__width = width

    def getWidth(self):
        return self.__width


class Line(Prop):
    def __init__(self, *args):
        print('__init__ Line')
        # Prop.__init__(self, *args)
        super().__init__(*args)
        self.__width = 5

    def drawLine(self):
        # print(f'draw line: {self._sp}, {self._ep}, {self._color}, {self.getWidth()}')
        print(f'draw line: {self._sp}, {self._ep}, {self._color}, {self.__width}')

class Rect(Prop):
    def drawRect(self):
        print(f'draw rect: {self._sp}, {self._ep}, {self._color}, {self.getWidth()}')



# print(issubclass(Point, object))

l = Line(Point(1, 2), Point(10, 20))
print(l.__dict__)
l.drawLine()

# r = Rect(Point(30, 40), Point(70, 80))
# r.drawRect()



