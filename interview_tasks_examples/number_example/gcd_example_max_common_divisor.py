# https://www.youtube.com/watch?v=0Bc8zLURY-c&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=7
# https://www.youtube.com/watch?v=yrOKPlg1TXg

# Рекурсия на пример НОД (наибольший общий делитель), алгоритм Евклида,
# O(log(min(a,b))
# https://www.youtube.com/watch?v=0Bc8zLURY-c&t=3546s


def gcd(a, b) -> int:
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)


def gcd_two(a, b) -> int:
    if b == 0:
        return a
    else:
        print(f"a = {a} , b = {b}, a % b = {a % b}")
        return gcd(b, a % b)


if __name__ == "__main__":
    out = gcd(40, 30)
    print(out)

    print(60 % 18)

    out = gcd_two(60, 18)
    print(out)

    out = gcd_two(18, 60)
    print(out)
