"""
https://www.patreon.com/oleg_molchanov/posts?filters[tag]=%23%D0%BA%D1%83%D1%80%D1%81%D0%9E%D0%9E%D0%9F
password: xau8ahPh
lesson №19
"""


class IntDescriptor:
    def __set__(self, instance, value):
        print(f"I got {value}")
        self._value = value

    def __get__(self, instance, owner):
        if instance is None:
            print("Call from a class")
            return self
        print("Call from instance")
        return self._value


class Vector:
    x = IntDescriptor()
    y = IntDescriptor()


if __name__ == "__main__":
    v1 = Vector()
    v1.x = 10
    print(v1.x)

    v2 = Vector()
    print(v2.x)
    print(v1.x)

    v2.x = 20
    print(v2.x)
    print(v1.x)
