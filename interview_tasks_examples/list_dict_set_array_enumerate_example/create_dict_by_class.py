class MyDictionary:
    def __init__(self, size):
        self.size = size

        self.keys = [None] * self.size
        # print(self.keys)

        self.value = [None] * self.size
        # print(self.value)

    def __setitem__(self, key, value):
        index = hash(key) % self.size
        print(f"index from set {index}")

        self.keys[index] = key
        self.value[index] = value

    def __getitem__(self, key):
        index = hash(key) % self.size
        print(f"index from get {index}")

        return self.value[index]


if __name__ == '__main__':
    d = MyDictionary(10)

    d["apple"] = "red"
    print(d["apple"])

    d["banana"] = "yellow"
    print(d["banana"])
