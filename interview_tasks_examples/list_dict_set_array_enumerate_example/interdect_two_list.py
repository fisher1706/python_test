def intersect_two_lists(list1, list2):
    res, list2_copy = [], list2[:]
    for el in list1:
        if el in list2_copy:
            res.append(el)
            list2_copy.remove(el)
    return res


if __name__ == "__main__":
    l1 = [3, 5, 7]
    l2 = [2, 4, 6, 3]

    print(intersect_two_lists(l1, l2))
