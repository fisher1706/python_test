# https://www.youtube.com/watch?v=9ayiLB20wRA&list=PLrzHY9riBq3bu8xnTqukuj_6JpWD8LFB5&index=18


def square_generator():
    for number in range(1, 5):
        yield number * number


if __name__ == "__main__":
    print(square_generator())

    for i in square_generator():
        print(i)


    gen = square_generator()

    for i in gen:
        print(i)

    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
