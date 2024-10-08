def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


# @coroutine
def subgen():
    x = "Ready to accept message"
    message = yield x
    print("Subgen received:", message)


class BlaBlaException(Exception):
    pass


@coroutine
def average():
    count = 0
    sum = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print("Done")
            break
        except BlaBlaException:
            print("..................................")
            break
        else:
            count += 1
            sum += x
            average = round(sum / count, 2)
    return average


if __name__ == "__main__":
    g = subgen()
    # next(g)

    g.send(None)
    g.send("Ok")
