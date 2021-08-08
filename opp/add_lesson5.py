class Point:
    __count = 0
    __instance = None

    def __new__(cls, *ars, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = super(Point, cls).__new__(cls)
        else:
            print('Экземпляр класса Point уже создан!')

    def __init__(self, x = 0, y = 0):
        Point.__count += 1
        self.x = x
        self.y = y

pt1 = Point()
pt2 = Point()
pt3 = Point()

print(id(pt1), id(pt2), id(pt3), sep='\n')