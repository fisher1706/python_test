# https://www.youtube.com/watch?v=0Bc8zLURY-c&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=7
# https://www.youtube.com/watch?v=yrOKPlg1TXg


def func_pow(a: float, number: int) -> float:
    if number == 0:
        return 1
    elif number % 2 == 1:
        return func_pow(a, number - 1) * a
    else:
        return func_pow(a**2, number // 2)


if __name__ == "__main__":
    out_pow = func_pow(5, 3)
    print(f"pow: {out_pow}")
