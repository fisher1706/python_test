# https://www.youtube.com/watch?v=hZ-Hb6jTfgQ&list=PLF4MWzDJPFSZJeqc7u65mRAjR-1eFKUfd&index=12

class A:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        new = A(self.x)
        new.x += other.x
        return new

    def __iadd__(self, other):
        self.x += other.x
        return self

    def __sub__(self, other):
        new = A(self.x)
        new.x -= other.x
        return new

    def __isub__(self, other):
        self.x -= other.x
        return self


    def __str__(self):
        return str(self.x)


obj1 = A(10)
obj2 = A(20)

# print(odj1 + obj2)

obj3 = A(30)
obj4 = A(40)

obj3 += obj4
print(obj3)

obj3 -= obj4
print(obj3)







