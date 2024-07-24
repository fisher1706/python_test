def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_dp(n):
    fib_values = [0, 1]
    for i in range(2, n + 1):
        fib_values.append(fib_values[i-1] + fib_values[i-2])
    return fib_values[n]


if __name__ == "__main__":
    num = 10

    out = fibonacci_recursive(num)
    print(out)

    out = fibonacci_dp(num)
    print(out)
