from collections import Counter


"""
Counter нужен для подсчета элементов в последовательности - работает только с hashable
"""


counter = Counter("hello")
counter.update("world")


if __name__ == "__main__":
    print(counter)
    print(counter.most_common(1))
    print(counter.most_common(3))
