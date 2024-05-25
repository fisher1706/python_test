def star_triangle(r):
    for x in range(r):
        # print(f"x=: {x}")
        # print(f"_=: {(r-x-1)}")
        # print(f"*=: {(2*x+1)}")
        print(" " * (r - x - 1) + "*" * (2 * x + 1))


if __name__ == "__main__":
    star_triangle(2)
