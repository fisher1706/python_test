def check_prime_number(number):
    if number > 1:
        for x in range(2, number):
            print(f"x=: {x}")
            print(f"div=: {number % x}")
            if number % x == 0:
                print("not prime")
                break
        else:
            print("Prime")
    else:
        print("not prime")


if __name__ == '__main__':
    n = 8
    check_prime_number(n)
