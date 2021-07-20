# https://www.youtube.com/watch?v=8cMMO8fks-k&list=PLQAt0m1f9OHvv2wxPGSCWjgy1qER_FvB6&index=51

def genf():
    s = 7
    for i in [43, 65, 32]:
        yield i
        print(s)
        s = s * 10 + 7

# s = genf()
# print(s)
# print(next(s))
# print(next(s))

def fact(n):
    pr = 1
    for i in range (1, n+1):
        pr = pr * i
        yield pr

for i in fact(10):
    print(i, end=' ')



