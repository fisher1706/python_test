# https://www.youtube.com/watch?v=P0uvWDpqB8I&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=17
import timeit

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc(self):
        self.a += 1
        del self.b
        self.b = 0

class Point2D:
    __slots__ = ('a', 'b')
    MAX_COORD = 100

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc(self):
        self.a += 1
        del self.b
        self.b = 0

pt = Point(1, 2)
pt2 = Point2D(12, 20)

print(pt.__sizeof__(), pt.__dict__.__sizeof__())
print(pt2.__sizeof__())

t1 = timeit.timeit(pt.calc)
t2 = timeit.timeit(pt2.calc)

print(t1, t2)

