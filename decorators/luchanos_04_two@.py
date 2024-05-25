# https://www.youtube.com/watch?v=tNkJ1gTnQDM&list=PLlKID9PnOE5h8VJyEiEd_Uv_-tt9KX7MD&index=4


def second_outer(**dkwargs):
    def outer(func):
        def inner(*args, **kwargs):
            attempts = dkwargs["attempts"]
            while attempts > 0:
                try:
                    return func(*args, **kwargs)
                except ZeroDivisionError as err:
                    print(f"Error: {err}, attempts left: {attempts}")
                    attempts -= 1

        return inner

    return outer


def simple_deco(func):
    def inner(*args, **kwargs):
        print("message")
        return func(*args, **kwargs)

    return inner


@simple_deco
@second_outer(attempts=5)
def div(a, b):
    return a / b


if __name__ == "__main__":
    print(div(1, 1))
