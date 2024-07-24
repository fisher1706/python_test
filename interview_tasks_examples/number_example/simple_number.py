def check_simple_number(num):
    if num > 1:
        for x in range(2, num):
            if num % x == 0:
                print("not prime")
                break
        else:
            print("Prime")
    else:
        print("not prime")


if __name__ == "__main__":
    check_simple_number(5)
