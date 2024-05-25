# TODO: method __del__ -> start after end program


class Point:
    color = "red"
    circle = 2

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print("delete exemplar: " + str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


if __name__ == "__main__":
    pt = Point(5, 10)
    print(pt.__dict__)
    print(pt.x, pt.y)

    pt.x = 100
    print(pt.__dict__)
