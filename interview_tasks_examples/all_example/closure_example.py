"""
Замыкание (closure) — это функция, которая сохраняет доступ к переменным в своей внешней области видимости,
даже если эта область видимости уже вышла из области действия.
"""


def outer(x):
    def inner():
        return f"x is {x}"

    return inner


if __name__ == "__main__":
    closure = outer(5)
    print(closure())
