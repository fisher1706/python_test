# https://www.youtube.com/watch?v=8cMMO8fks-k&list=PLQAt0m1f9OHvv2wxPGSCWjgy1qER_FvB6&index=51

def genf():
    out = 7
    for item in [43, 65, 32]:
        yield item
        print(out)
        out = out * 10 + 7


def fact(n):
    pr = 1
    for item in range(1, n+1):
        pr = pr * item
        yield pr


if __name__ == '__main__':
    s = genf()
    print(s)
    print(next(s))
    print(next(s))
    print(next(s))
    print("*" * 200)

    for i in fact(10):
        print(i, end=' ')
