def modify_list(lst: list) -> list:
    lst.append(4)
    lst = [1, 2, 3]
    return lst


if __name__ == '__main__':
    x = [0]
    y = modify_list(x)

    print(x)
    print(y)
