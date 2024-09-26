def squares(number):
    val = 1
    while val <= number:
        yield val**2
        val += 1


if __name__ == "__main__":
    n = 7
    for i in squares(n):
        print(f"i=: {i}")

    print(type(squares))

    gen = squares(3)
    print(type(gen))
