# https://www.youtube.com/watch?v=0Bc8zLURY-c&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=7
# https://www.youtube.com/watch?v=yrOKPlg1TXg


import graphics as gr


def fractal_rectangle(inner_window, a, b, c, d, alpha, deep=50):
    if deep < 1:
        return
    for p1, p2 in (a, b), (b, c), (c, d), (d, a):
        gr.Line(gr.Point(*p1), gr.Point(*p2)).draw(inner_window)
    a1 = (a[0] * (1 - alpha) + b[0] * alpha, a[1] * (1 - alpha) + b[1] * alpha)
    b1 = (b[0] * (1 - alpha) + c[0] * alpha, b[1] * (1 - alpha) + c[1] * alpha)
    c1 = (c[0] * (1 - alpha) + d[0] * alpha, c[1] * (1 - alpha) + d[1] * alpha)
    d1 = (d[0] * (1 - alpha) + a[0] * alpha, d[1] * (1 - alpha) + a[1] * alpha)
    fractal_rectangle(inner_window, a1, b1, c1, d1, alpha, deep - 1)


def main():
    # Set the graphics library
    window_main = gr.GraphWin("Fractal Rectangle", 600, 600)
    window_main.setBackground("white")
    # The initial settings
    alpha = 0.1
    a, b, c, d = (100, 100), (500, 100), (500, 500), (100, 500)
    fractal_rectangle(window_main, a, b, c, d, alpha)
    # Close the window
    window_main.getMouse()


def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)


def gcd_two(a, b) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def matryoshka(number: int) -> None:
    if number == 1:
        print("matryoshka")
    else:
        print(f"top: {number}")
        matryoshka(number - 1)
        print(f"down: {number}")


def func_pow(a: float, number: int) -> float:
    if number == 0:
        return 1
    elif number % 2 == 1:
        return func_pow(a, number - 1) * a
    else:
        return func_pow(a**2, number // 2)


def hanoi(number, source, auxiliary, target):
    if number > 0:
        # Переместить n-1 дисков с source на auxiliary, используя target как вспомогательный
        hanoi(number - 1, source, target, auxiliary)

        # Переместить оставшийся диск с source на target
        print(f"Переместить диск {number} с {source} на {target}")

        # Переместить n-1 дисков с auxiliary на target, используя source как вспомогательный
        hanoi(number - 1, auxiliary, source, target)


if __name__ == "__main__":
    matryoshka(5)

    # main()

    out = gcd(40, 30)
    print(out)

    print(60 % 18)

    out = gcd_two(60, 18)
    print(out)

    out_pow = func_pow(5, 3)
    print(f"pow: {out_pow}")

    n = 3  # Количество дисков
    hanoi(n, "A", "B", "C")
