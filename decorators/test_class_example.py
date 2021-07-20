import pprint
import math

def adv_deco(password):
    def adv_deco_inner(my_class):
        def inner(*args, **kwargs):
            secret_pass = 123
            if password != secret_pass:
                raise ValueError('Bad password!')
            print('zapel')
            return my_class(*args, **kwargs)
        return inner
    return adv_deco_inner

@adv_deco(password=123)
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


obj = MyClass(1, 2)

print(obj)

pprint.pprint(locals())
pprint.pprint(dir(math))
