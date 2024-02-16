a = [1, 2, 3]
c = a
b = [1, 2, 3]


if __name__ == '__main__':
    print(id(a))
    print(id(b))
    print(id(c))
    