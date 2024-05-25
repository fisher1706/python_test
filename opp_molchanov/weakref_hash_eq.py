"""
https://www.patreon.com/oleg_molchanov/posts?filters[tag]=%23%D0%BA%D1%83%D1%80%D1%81%D0%9E%D0%9E%D0%9F
password: xau8ahPh
lesson №20
"""


class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, obj):
        return isinstance(obj, Person) and self.name == obj.name

    def __hash__(self):
        return hash(self.name)


if __name__ == "__main__":
    p = Person("Ivan")
    print(hash(p))
