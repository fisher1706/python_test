def count_path_one(n):
    k = [0, 1] + [0] * n
    for i in range(2, n + 1):
        k[i] = k[i - 2] + k[i - 1]
    return k[n]


def count_path_two(n: int, allowed: list):
    k = [0, 1, allowed[2]] + [0] * (n - 3)
    for i in range(3, n + 1):
        if allowed[i]:
            k[i] = k[i - 1] + k[i - 2] + k[i - 3]
    return k[n]


def count_min_price(n: int, price: list):
    c = [float("-inf"), price[1], price[2] + [0] * (n - 2)]
    for i in range(3, n + 1):
        c[i] = price[i] + min(c[i - 1], price[i - 2])
    return c[n]


if __name__ == '__main__':
    print(count_path_one(3))
