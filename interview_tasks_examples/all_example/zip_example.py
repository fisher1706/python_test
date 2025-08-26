if __name__ == "__main__":
    # Пример использования zip для объединения списков
    print(
            list(
                zip(
                    [1, 2, 3],
                    ["apple", "grape", "orange"],
                    ["x", 2, True]
                )
            )
        )
    print("*" * 100)


    # Пример использования zip для объединения списков
    for num, fruit, thing in zip(
        [1, 2, 3],
        ["apple", "grape", "orange"],
        ["zero", 2, True]
    ):
        print(f"num = {num}")
        print(f"fruit = {fruit}")
        print(f"thing = {thing}")
    print("*" * 100)


    # Пример использования zip для объединения списков и создания словаря
    s = "abc"
    t = (10, 20, 30, 40)
    print(dict(zip(s, t)))
