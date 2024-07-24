# https://www.youtube.com/watch?v=lgHS8SoEsB0
def sieve_of_eratosthenes(number: int):
    primes = [True] * number
    primes[0] = primes[1] = False
    p = 2

    for k in range(2, number):
        if primes[p]:
            for i in range(2 * k, number, k):
                primes[i] = False

    prime_numbers = [p for p in range(2, number) if primes[p]]
    return prime_numbers


if __name__ == '__main__':
    n = 30

    print(f"Простые числа до {n}: {sieve_of_eratosthenes(n)}")
    