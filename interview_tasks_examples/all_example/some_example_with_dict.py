a = {}

a[1] = 1
a[2] = 2

a[1] = a[1] + 1


if __name__ == '__main__':
    count = 0
    for i in a:
        count += a[i]
        print(count)


