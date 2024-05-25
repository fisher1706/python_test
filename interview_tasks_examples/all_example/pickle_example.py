import pickle

a = 1

if __name__ == "__main__":
    # pickling
    pickle.dump(a, open("../file.txt", "wb"))

    # unpickling
    file = pickle.load(open("../file.txt", "rb"))
    print(file)
