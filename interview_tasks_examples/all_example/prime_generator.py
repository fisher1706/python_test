def prime_generator():
    for number in range(1, 1001):
        i = 2
        factor = 0
        while i < number:
            if number % i == 0:
                factor += 1
            i += 1
        if factor == 0 and number > 1:
            yield number


if __name__ == "__main__":
    prime_no = prime_generator()

    print(next(prime_no))
    print(next(prime_no))
    print(next(prime_no))
    print(next(prime_no))
