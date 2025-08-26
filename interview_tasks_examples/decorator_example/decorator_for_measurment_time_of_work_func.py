from datetime import datetime
import time


def func_wrapper_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        delta_time = datetime.now() - start
        print(f"execution_time: {delta_time}")
        return result

    return wrapper


@func_wrapper_time
def func_1():
    time.sleep(1)


@func_wrapper_time
def func_2():
    time.sleep(2)


if __name__ == "__main__":
    func_1()
    func_2()
