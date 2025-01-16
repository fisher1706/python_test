def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)


def square(num):
    return triangle(num) + triangle(num - 1)


if __name__ == '__main__':
    print(triangle(5))
    print(square(5))