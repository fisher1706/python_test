my_list = [1, 2, 3]

if __name__ == "__main__":
    my_list.append(4)
    print(my_list)
    print("*" * 100)

    count = my_list.count(2)
    print(count)
    print("*" * 100)

    new_list = my_list.copy()
    print(new_list)
    print("*" * 100)

    my_list.reverse()
    print(my_list)
    print("*" * 100)

    print("___remove___")
    my_list.append(3)
    print(my_list)
    my_list.remove(3)
    print(my_list)
    print("*" * 100)

    my_list.insert(0, 9)
    print(my_list)
    print("*" * 100)

    print("___pop___")
    my_list.pop()
    print(my_list)
    print("*" * 100)

    my_list.pop(0)
    print(my_list)
    print("*" * 100)

    my_list.sort()
    print(my_list)
    print("*" * 100)

    my_list.clear()
    print(my_list)
    print("*" * 100)
