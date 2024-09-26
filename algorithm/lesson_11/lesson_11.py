# https://www.youtube.com/watch?v=m4HOkVeN4Mo&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=11
# https://www.youtube.com/watch?v=t2DpD9GnhfU


def lcs(a: list, b: list) -> int:
    f = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    print(f)

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                f[i][j] = f[i - 1][j - 1] + 1
            else:
                f[i][j] = max(f[i - 1][j], f[i][j - 1])
    return f[-1][-1]


def lis_example(a):
    """Возвращает длину наибольшей возрастающей подпоследовательности"""
    f = [0] * (len(a) + 1)
    for i in range(1, len(a) + 1):
        m = 0  # максимум
        for j in range(0, i):
            if a[i - 1] > a[j - 1] and f[j] > m:
                m = f[j]
        f[i] = m + 1
    return max(*f)


if __name__ == "__main__":
    A = [1, 2, 3, 4, 8, 9, 7, 8]
    B = [1, 2, 8, 3]

    print(lcs(A, B))

    print(lis_example(A))
