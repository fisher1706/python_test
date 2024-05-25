from collections import OrderedDict

"""
OrderedDict - нужен для действий со словарем где необходим порядок элементов, сравнение с учетом порядка, 
перестановка элементов с сохранением порядка. Занимает в два раза больше памяти по сравнению с обычным словарем.
"""

first = {1: 1, 2: 2, 3: 3, 4: 4}
second = {2: 2, 1: 1, 3: 3, 4: 4}


order_1 = OrderedDict(first)
order_2 = OrderedDict(second)


if __name__ == '__main__':
    print(first == second)
    print(order_1 == order_2)
    print(order_1)

    print(order_1.popitem())
    print(order_1)

    print(order_2.popitem(last=False))
    print(order_2)

    order_1.move_to_end(1)
    print(order_1)

    order_1.move_to_end(3, last=False)
    print(order_1)
