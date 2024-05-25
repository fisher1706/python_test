"""
https://www.patreon.com/oleg_molchanov/posts?filters[tag]=%23%D0%BA%D1%83%D1%80%D1%81%D0%9E%D0%9E%D0%9F
password: xau8ahPh
lesson №20
"""

import weakref


class Person:
    pass


if __name__ == "__main__":
    p = Person()
    print(p)

    w = weakref.ref(p)
    print(w)
    print(w())

    del p
    print(w)
    print(w())

    p = Person()
