# https://www.youtube.com/watch?v=VrhfCh5Pp6E&list=PLhqLR-FtmNaXXnYQ7tsy2Fw7USL14fdfB&index=4

def check_triangle_number(n: int) -> bool:
    row = 1

    if not isinstance(n, int):
        return False

    while n > 0:
        n -= row
        row += 1

    return n == 0


if __name__ == '__main__':
    num = 0

    out = check_triangle_number(num)
    print(out)
