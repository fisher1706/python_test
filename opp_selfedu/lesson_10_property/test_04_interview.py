"""
@property декоратор может быть использован для определения методов в классе, которые действуют как атрибуты.
"""


class Person:
    def __init__(self, name, old):
        self._name = name
        self._old = old

    @property
    def old(self):
        return self._old

    @old.setter
    def old(self, old):
        self._old = old

    @old.deleter
    def old(self):
        del self._old


if __name__ == "__main__":
    p = Person("oleg", 40)
    print(p.__dict__)

    del p.old
    print(p.__dict__)

    p.old = 20
    print(p.__dict__)
