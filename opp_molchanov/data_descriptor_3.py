"""
https://www.patreon.com/oleg_molchanov/posts?filters[tag]=%23%D0%BA%D1%83%D1%80%D1%81%D0%9E%D0%9E%D0%9F
password: xau8ahPh
lesson №19
"""

import ctypes


class IntDescriptor:
    def __init__(self):
        self._values = {}

    def __set__(self, instance, value):
        self._values[instance] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._values.get(instance)


class Vector:
    x = IntDescriptor()
    y = IntDescriptor()


def ref_count(obj_id):
    return ctypes.c_long.from_address(obj_id).value


if __name__ == "__main__":
    v1 = Vector()
    print(v1.x)

    v2 = Vector()
    print(v2.x)

    v1.x = 5
    print(v1.x)

    v2.x = 10
    print(v2.x)

    print(Vector.x._values)

    v3 = Vector()
    ref_count_start = ref_count(id(v3))
    print(ref_count_start)

    id_v = id(v3)
    print(id_v)

    v3.x = 5
    v3.y = 10

    ref_count_end = ref_count(id_v)
    print(ref_count_end)

    del v3
    print(ref_count(id_v))
