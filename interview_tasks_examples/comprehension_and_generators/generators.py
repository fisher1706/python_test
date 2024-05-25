"""
Генератор - одноразовый - нужно создавать новый генератор в следующем случае
"""


ints = [-5, 8, -2, 1, 2, 3]
positive_gen = (e for e in ints if e > 0)


if __name__ == '__main__':
    print(positive_gen)
    print(next(positive_gen))

    for i in positive_gen:
        print(i)
