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


if __name__ == '__main__':
    A3 = [1, 2, 3, 4, 5]
    A4 = [1, 2, 3, 4, 5]

    shift_left(A3, 1)

    shift_right(A4, 1)
