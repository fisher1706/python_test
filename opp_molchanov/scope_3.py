"""
https://www.patreon.com/oleg_molchanov/posts?filters[tag]=%23%D0%BA%D1%83%D1%80%D1%81%D0%9E%D0%9E%D0%9F
password: xau8ahPh
lesson №10
"""


class Config:
    name = 'Igor'
    # pass


class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_file(cls, path):
        with open(path) as f:
            name = f.read().strip()
        return cls(name=name)

    @classmethod
    def from_obj(cls, obj):
        if hasattr(obj, 'name'):
            name = getattr(obj, 'name')
            return cls(name=name)
        return cls



if __name__ == '__main__':
    path = 'text_scope.txt'
    print(Config.__dict__)

    p = Person('oleg')
    print(p.__dict__)

    d = Person.from_file(path)
    print(d.__dict__)

    z = Person.from_obj(Config)
    print(z.__dict__)



