from pprint import pprint


class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left


if __name__ == "__main__":
    pprint(Point.__dict__)
    pt1 = Point(1, 2)
    pt2 = Point(10, 20)

    pt1.set_bound(-100)
    print(pt1.__dict__)
    pprint(Point.__dict__)
