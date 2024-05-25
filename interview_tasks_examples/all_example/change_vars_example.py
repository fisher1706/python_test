def change_first(var1, var2):
    var1, var2 = var2, var1
    print(f"x:={var1}, y:={var2}")


def change_second(var1, var2):
    var2 = var1 + var2
    var1 = var2 - var1
    var2 = var2 - var1
    print(f"x:={var1}, y:={var2}")


if __name__ == "__main__":
    x = 3
    y = 4

    change_first(x, y)
    change_second(x, y)
