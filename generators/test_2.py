# https://www.youtube.com/watch?v=yPh7ZJr-A0E
# https://www.youtube.com/watch?v=xGb-MusLAmk

from datetime import datetime
import sys

def func(n):
    res = []
    cnt = 0

    while cnt < n:
        res.append(cnt)
        cnt += 1
    return res

def func_2():
    print('пришли')
    yield 1
    print('дай еще')
    yield 2
    print('ушли')

def func_3(n):
    cnt = 0

    while cnt < n:
        yield (cnt)
        cnt += 1


# print(func)
# print(func_2)
#
#
# print(func(10))
# print(func_2())


# c = func_2()
# print(next(c))
# print('основной поток')
# print(next(c))
# print('основной поток')
# print(next(c))

# d = func_3(10)
# print(next(d))
# print(next(d))
# print(next(d))

# l = func(100_000)
d = func_3(100_000)

try:
    while True:
        next(d)
except:
    print('finished')

start = datetime.now()
print(f'start: {start}')

print(f'size: {sys.getsizeof(d)}')
print(f'finish: {datetime.now()}. work: {datetime.now() - start}')

c = func_3(10)

print(3 in c)
print(list(c))