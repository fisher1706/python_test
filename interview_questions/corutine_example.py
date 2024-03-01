# https://www.geeksforgeeks.org/coroutine-in-python/


def print_name(prefix):
    print("Searching prefix: {}".format(prefix))
    while True:
        name = yield
        if prefix in name:
            print(name)


coroutine = print_name("Dear")
coroutine.__next__()


if __name__ == '__main__':
    coroutine.send("Atul")
    coroutine.send("Dear Atul")
