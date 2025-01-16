def factorial(num):
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


if __name__ == '__main__':
    print(factorial(6))