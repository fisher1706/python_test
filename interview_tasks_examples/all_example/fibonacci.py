def fibonacci(n):
    i = 1
    n1 = 0
    n2 = 1

    while i <= n:
        fab_no = n1+n2
        print(fab_no)
        n1, n2 = n2, fab_no
        i += 1


if __name__ == '__main__':
    num = 3
    fibonacci(num)
