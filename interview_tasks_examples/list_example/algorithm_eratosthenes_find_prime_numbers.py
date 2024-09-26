# https://www.youtube.com/watch?v=lgHS8SoEsB0
# https://www.youtube.com/watch?v=FTBFWYuKsM0


def sieve_of_eratosthenes(number):
    # Изначально все числа считаются простыми (True)
    primes = [True] * (number + 1)
    p = 2

    while p * p <= number:
        # Если primes[p] не был изменен, то это простое число
        if primes[p]:
            # Обновляем все кратные p начиная с p^2
            for i in range(p * p, number + 1, p):
                primes[i] = False
        p += 1

    # Возвращаем все простые числа
    return [p for p in range(2, number + 1) if primes[p]]


if __name__ == "__main__":
    n = 20

    print(f"Простые числа до {n}: {sieve_of_eratosthenes(n)}")
