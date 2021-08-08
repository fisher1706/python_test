class Doctor:
    def __init__(self, degree):
        self.degree = degree

    def can_cure(self):
        print('Я могу лечить.')

    def can_build(self):
        print('Я доктор, я могу строить.')

    def graduate(self):
        print('Я отучился на доктора.')


class Builder:
    def __init__(self, rank):
        self.rank = rank

    def can_build(self):
        print('Я могу строить.')

    def graduate(self):
        print('Я отучился на строителя.')


class Person(Doctor, Builder):
    def __init__(self, degree, rank):
        # self.degree = degree
        # self. rank = rank

        super().__init__(degree)
        Builder.__init__(self, rank)

    def can_build(self):
        print('Я человек, я могу строить.')

    def graduate(self):
        print('Кто я?.')
        super().graduate()
        Builder.graduate(self)

    def __str__(self):
        return f'Person: {self.degree} - {self.rank}'

s = Person('spec', 5)

# s.can_build()
# s.can_cure()

# print(Person.__mro__)

s.graduate()

print(s)