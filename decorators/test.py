def second_outer(*dargs, **dkwargs): # параметры декоратора
    def outer(func): # функция
        def inner(*args, **kwargs): # параметры функции
            attempts = dkwargs['attempts']
            while attempts > 0:
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    print(f'Error: {err}, attemps_left: {attempts}')
                    attempts -= 1
        return inner
    return outer

def simple_deco(func):
    def inner(*args, **kwargs):
        print('zapel')
        return func(*args, **kwargs)
    return inner

@simple_deco
@second_outer(attempts=5)
def div(a, b):
    return a / b

print(div(1, 0))
