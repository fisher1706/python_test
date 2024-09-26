# https://www.youtube.com/watch?v=NLq7nB9bV0M
# https://www.youtube.com/watch?v=dAAkElskMmU


"""
O(n^2)
"""


def insert_sort(data: list) -> list:
    n = len(data)
    for top in range(1, n):
        k = top
        while k > 0 and data[k - 1] > data[k]:
            data[k], data[k - 1] = data[k - 1], data[k]
            k -= 1
    return data


def choice_sort(data: list) -> list:
    n = len(data)
    for pos in range(0, n - 1):
        for k in range(pos + 1, n):
            if data[k] < data[pos]:
                data[k], data[pos] = data[pos], data[k]
    return data


def bubble_sort(data: list) -> list:
    n = len(data)
    for bypass in range(1, n):
        for k in range(0, n - bypass):
            if data[k] > data[k + 1]:
                data[k], data[k + 1] = data[k + 1], data[k]
    return data


"""
O(n), O(m) -> m - quantity of different elements
"""


def count_sort(data: list) -> list:
    """
    числа от 0 до 9 - диапазон f
    """
    f = [0] * 10

    for x in data:
        f[x] += 1

    print(f)

    inner = [[i] * f[i] for i in range(len(f)) if f[i]]
    sorted_list = [i for val in inner for i in val]
    return sorted_list


if __name__ == "__main__":
    my_list = [4, 2, 2, 5, 1, 3]

    out_insert = insert_sort(my_list)
    print(out_insert)

    out_choice = choice_sort(my_list)
    print(out_choice)

    out_bubble = bubble_sort(my_list)
    print(out_bubble)

    out_count = count_sort(my_list)
    print(out_count)
