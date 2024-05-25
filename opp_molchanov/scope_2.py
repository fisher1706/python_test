"""
https://www.patreon.com/oleg_molchanov/posts?filters[tag]=%23%D0%BA%D1%83%D1%80%D1%81%D0%9E%D0%9E%D0%9F
password: xau8ahPh
lesson №10
"""


class Person:
    name = "Dima"

    @classmethod
    def change_name(cls, name):
        cls.name = name


if __name__ == "__main__":
    p = Person()
    print(p.__dict__)
    p.change_name("zapel")

    print("instance dict: ", p.__dict__)
    print("person.name: ", Person.name)
