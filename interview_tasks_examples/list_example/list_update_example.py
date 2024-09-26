lst1 = [2, 2]
lst2 = [2, 6]

lst1[1] *= 2
lst2[1] -= 2


if __name__ == "__main__":
    print(lst1)
    print(lst2)

    print(int(lst1 is lst2))
