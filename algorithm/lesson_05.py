# https://www.youtube.com/watch?v=3I6OjxoeSS8


def func_one(data: list) -> None:
    for i in data:
        print(i)
        i += 1
        print(i)

    print("*" * 200)
    for i in data:
        print(i)


def update_every_element_of_list(data: list) -> None:
    for i in range(len(data)):
        data[i] = data[i] + 1
    print(data)


def replace_elements_of_list(data: list) -> None:
    for i in range(len(data) // 2):
        data[i], data[len(data) - i - 1] = data[len(data) - i - 1], data[i]
    print(data)


def shift_left(data: list, k: int) -> None:
    len_data = len(data)
    k = k % len_data  # В случае если k больше длины списка
    for _ in range(k):
        tmp = data[0]
        for i in range(len_data - 1):
            data[i] = data[i + 1]
        data[-1] = tmp
    print(data)


def shift_right(data: list, k: int) -> None:
    len_data = len(data)
    k = k % len_data  # В случае если k больше длины списка
    for _ in range(k):
        tmp = data[-1]
        for i in range(len_data - 1, 0, -1):
            data[i] = data[i - 1]
        data[0] = tmp
    print(data)


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


if __name__ == "__main__":
    A1 = [1, 2, 3, 4, 5]
    A2 = [1, 2, 3, 4, 5]
    A3 = [1, 2, 3, 4, 5]
    A4 = [1, 2, 3, 4, 5]

    func_one(A1)

    update_every_element_of_list(A1)

    replace_elements_of_list(A2)

    shift_left(A3, 1)

    shift_right(A4, 1)

    n = 30
    print(f"Простые числа до {n}: {sieve_of_eratosthenes(n)}")
