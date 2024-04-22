"""
https://www.patreon.com/oleg_molchanov/posts?filters[tag]=%23%D0%BA%D1%83%D1%80%D1%81%D0%9E%D0%9E%D0%9F
password: xau8ahPh
lesson №10
"""


name = 'Ivan'


class Person:
    name = 'Dima'

    def print_name_1(self):
        print(name)

    def print_name_2(self):
        print(self.name)



if __name__ == '__main__':
    p = Person()

    p.print_name_1()
    p.print_name_2()

    print(p.__dict__)
    p.print_name_2()

    p.name = 'zapel'
    print('instance dict: ', p.__dict__)
    print('person.name: ', Person.name)


