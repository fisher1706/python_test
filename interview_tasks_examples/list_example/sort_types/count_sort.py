# https://www.youtube.com/watch?v=NLq7nB9bV0M
# https://www.youtube.com/watch?v=dAAkElskMmU


def count_sort(data: list) -> list:
    """
    числа от 0 до 9 - диапазон f
    """
    f = [0] * (len(data) + 1)

    for x in data:
        f[x] += 1

    print(f)

    inner = [[i] * f[i] for i in range(len(f)) if f[i]]
    print(f"inner: {inner}")

    sorted_list = [i for val in inner for i in val]
    return sorted_list


if __name__ == "__main__":
    my_list = [0, 4, 2, 2, 0, 5, 1, 3]

    out_count = count_sort(my_list)
    print(out_count)
