def largest_number(some_number):
    return 10**some_number - 1, len(str(10**some_number - 1))


if __name__ == "__main__":
    num = 10
    a, b = largest_number(num)
    print(a, b)
