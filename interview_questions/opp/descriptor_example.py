# class descriptor
class Ten:
    def __get__(self, instance, owner):
        return 10


class A:
    x = 5
    y = Ten()


if __name__ == "__main__":
    a = A()
    print(a.x, a.y)
    print(a.__dict__)
    print(A.__dict__)
