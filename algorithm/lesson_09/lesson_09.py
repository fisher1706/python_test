# https://www.youtube.com/watch?v=qf82-r9hl2Y&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=9


def merge_one(a: list, b: list) -> list:
    c = [0] * (len(a) + len(b))
    i = k = h = 0
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            c[h] = a[i]
            i += 1
            h += 1
        else:
            c[h] = b[k]
            k += 1
            h += 1
    while i < len(a):
        c[h] = a[i]
        i += 1
        h += 1
    while k < len(b):
        c[h] = b[k]
        k += 1
        h += 1
    return c


def merge_sort(a: list):
    if len(a) <= 1:
        return a

    middle = len(a) // 2

    left = [a[i] for i in range(0, middle)]
    # print(f"left: {left}")

    right = [a[i] for i in range(middle, len(a))]
    # print(f"right: {right}")

    merge_sort(left)
    merge_sort(right)

    c = merge_one(left, right)

    for i in range(len(a)):
        a[i] = c[i]

    print(f"a: {a}")


def hoar_sort(a: list):
    if len(a) <= 1:
        return

    left = []
    middle = []
    right = []

    barrier = a[0]

    for x in a:
        if x < barrier:
            left.append(x)
        elif x == barrier:
            middle.append(x)
        else:
            right.append(x)

    hoar_sort(left)
    hoar_sort(right)

    k = 0
    for x in left + middle + right:
        a[k] = x
        k += 1

    print(a)


def check_sorted(a: list, ascending: bool = True) -> bool:
    flag = True
    s = 2 * int(ascending) - 1

    for i in range(len(a)):
        if s * a[i] > s * a[i + 1]:
            flag = False
            break
    return flag


if __name__ == '__main__':
    one = [1, 3, 5, 7]
    two = [2, 4, 6, 8]
    three = [3, 1, 2, 6, 8, 9, 8, 7, 8, 3, 5, 7]

    out = merge_one(one, two)
    print(out)
    print("*" * 200)

    # merge_sort(three)
    # print("*" * 200)
    #
    # hoar_sort(three)
