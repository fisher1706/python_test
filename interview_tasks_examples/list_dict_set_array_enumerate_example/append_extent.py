a = [1, 2, 3]
b = [4, 5, 6]


if __name__ == '__main__':
    """
    join to lists
    """
    a.extend(b)
    print(a)
    print('*' * 100)

    """
    equal to "extend"
    """
    c = a + b
    print(c)
    print('*' * 100)

    """
    add list[b] to list[a] as element of list
    """
    a.append(b)
    print(a)
