from collections import ChainMap

"""
ChainMap - нужен для логического объединения словарей, поиска информации в них, 
по при изменениях меняется только первый словарь.
"""


first = {1: 1, 2: 2, 3: 3, 4: 4}
second = {2: 2, 1: 1, 3: 3, 4: 4}

chain = ChainMap(first, second)


if __name__ == "__main__":
    print(chain)

    print(1 in chain)
    print(5 in chain)

    first[1] = 1000
    print(chain)

    chain[1] = 1000
    chain[4] = 1000
    print(chain)
