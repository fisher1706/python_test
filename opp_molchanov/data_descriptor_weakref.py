"""
https://www.patreon.com/oleg_molchanov/posts?filters[tag]=%23%D0%BA%D1%83%D1%80%D1%81%D0%9E%D0%9E%D0%9F
password: xau8ahPh
lesson №20
"""


from weakref import WeakKeyDictionary


class IntDescriptor:
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __set__(self, instance, value):
        self._values[instance] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._values.get(instance)


class Vector:
    x = IntDescriptor()
    y = IntDescriptor()



if __name__ == '__main__':
    v = Vector()
    print(hex(id(v)))

    v.x = 10
    print(Vector.x._values.keyrefs())

    del v
    print(Vector.x._values.keyrefs())
