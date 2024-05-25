colors_list = ["red", "blue", "green"]
colors_dict = {"a": "red", "b": "blue", "c": "green"}


def fun(a, b, c):
    print(a, b, c)


if __name__ == "__main__":
    fun(*colors_list)
    print("*" * 200)

    fun(**colors_dict)
