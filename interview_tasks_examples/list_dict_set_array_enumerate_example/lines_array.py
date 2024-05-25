def get_zero(outer):
    num = None
    for inner in outer:
        for i in range(len(inner)):
            if inner[i] == 0:
                num = i
                for y in range(len(inner)):
                    inner[y] = 0
    return num


def replace(outer, num):
    for inner in outer:
        inner[num] = 0

    for i in outer:
        print(i)


if __name__ == "__main__":
    data = [[1, 2, 3], [1, 5, 5], [1, 4, 0]]

    n = get_zero(data)
    print(n)

    replace(data, n)
