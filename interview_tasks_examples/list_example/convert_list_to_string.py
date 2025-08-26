xs = [1, 2, 3]
s = "".join(str(x) for x in xs)

b = " marries ".join(list(["Alice", "Bob", "Oleg"]))

if __name__ == "__main__":
    print(s)
    print(b)
