# https://www.youtube.com/watch?v=M9XG1iOua7c&list=PLlKID9PnOE5h8VJyEiEd_Uv_-tt9KX7MD&index=3


def second_outer(*dargs, **dkwargs):
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


@second_outer(attempts=5)
def div(a, b):
    return a / b


if __name__ == '__main__':
    print(div(1, 0))
