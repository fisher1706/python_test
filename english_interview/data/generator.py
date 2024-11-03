"""
Generators yield values one at a time, conserving memory.
"""


def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1


if __name__ == '__main__':
    for number in count_up_to(5):
        print(number)
