import sys

a = [1, 2, 3]
b = a


if __name__ == "__main__":
    print(sys.getrefcount(a))
