my_list = [1, 2, 3]

if __name__ == "__main__":
    my_list.append(4)
    print(my_list)

    count = my_list.count(2)
    print(count)

    new_list = my_list.copy()
    print(new_list)

    my_list.reverse()
    print(my_list)

    my_list.remove(3)
    print(my_list)

    my_list.insert(0, 9)
    print(my_list)

    my_list.pop()
    print(my_list)

    my_list.pop(2)
    print(my_list)

    my_list.sort()
    print(my_list)

    my_list.clear()
    print(my_list)
