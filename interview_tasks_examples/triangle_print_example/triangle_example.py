def triangle(data):
    for i in range(data):
        if i % 2 != 0:
            print(' '*int((data-i)/2) + '*'*i + ' '*int((data-i)/2))


if __name__ == '__main__':
    triangle(9)
