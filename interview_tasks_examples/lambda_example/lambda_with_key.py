a = {1: 1, 2: 3, 3: 1}

if __name__ == "__main__":
    print(max(a, key=lambda x: a[x]))
    print(max(a))
