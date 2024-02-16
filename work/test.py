import random


def counter(number=5):
    slave = [random.randint(0, 1) for _ in range(number)]
    print('slave: ', slave)

    if not number % 2 == 0:
        number += 1
        master = [0 if x % 2 else 1 for x in range(number)]
        master.pop(0)
    else:
        master = [0 if x % 2 else 1 for x in range(number)]
    print('master: ', master)

    result = [0 if master[i] == slave[i] else 1 for i in range(len(master))]
    print('count: ', sum(result))

    return sum(result)


if __name__ == '__main__':
    counter()
