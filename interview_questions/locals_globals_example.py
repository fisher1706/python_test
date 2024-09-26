print(globals())


def summ(a, b):
    print(locals())
    return a + b


if __name__ == "__main__":
    summ(5, 10)
