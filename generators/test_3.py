# https://www.youtube.com/watch?v=uLZuSBZPzeY&list=PLlk6xtbRU2nCRtNLzci6OW9OjXMoe2-S_&index=21
# https://www.youtube.com/watch?v=rvV7v9s4HbQ&list=PLlk6xtbRU2nCRtNLzci6OW9OjXMoe2-S_&index=22

def range(start, stop):
    current = start

    while current < stop:
        reset = yield current
        if reset is not None:
            current = reset - 1
        current += 1

def two_ranges(start, stop):
    # for x in range(start, stop):
    #     yield x
    # for x in range(start, stop):
    #     yield x
    yield from range(start, stop)
    yield from range(start, stop)


g = range(0, 3)

# for i in g:
#     print(i)

# print(next(g))
# print(next(g))
# print(g.send(0))
# print(next(g))

g = two_ranges(0, 3)
print(next(g))
print(next(g))
# print(g.send(-1))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
