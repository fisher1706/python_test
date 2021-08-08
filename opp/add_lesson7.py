# https://www.youtube.com/watch?v=LVv8V94eZ9Y&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=7

class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __str__(self):
        return f'{self._x}, {self._y}'

    def isDigit(self):
        if isinstance(self._x, int) or isinstance(self._x, float) and \
           isinstance(self._y, int) or isinstance(self._y, float):
            return True
        return False

    def isInt(self):
        if isinstance(self._x, int) and isinstance(self._y, int):
            return True
        return False

class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def setCoords(self, sp, ep):
        if sp.isDigit() and ep.isDigit():
            self._sp = sp
            self._ep = ep
        else:
            print('must digit')


class Line(Prop):
    def drawLine(self):
        print(f'draw line: {self._sp}, {self._ep}, {self._color}, {self._width}')

    def __setOneCoor(self, sp):
        if sp.isInt():
            self._sp = sp
        else:
            print('coord must int')

    def setTwoCoor(self, sp, ep):
        if sp.isInt() and ep.isInt():
            Prop.setCoords(self, sp, ep)
        else:
            print('must int')

    def setCoords(self, sp: Point, ep: Point = None):
        if ep is None:
            self.__setOneCoor(sp)
        else:
            self.setTwoCoor(sp, ep)



l = Line(Point(1, 2), Point(10, 20))
l.drawLine()

l.setCoords(Point(10.1, 20), Point(100, 200))
l.drawLine()

l.setCoords(Point(-10, -20))
l.drawLine()





