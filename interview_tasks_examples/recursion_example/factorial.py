def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    result = 1
    for item in range(2, n + 1):
        result *= item
    return result


if __name__ == "__main__":
    print(factorial_iterative(7))
    print(factorial_recursive(0))
    print("*" * 200)

    for i in range(5):
        print(i)
