# https://www.youtube.com/watch?v=zBpIhPhTc9c&list=PLF4MWzDJPFSZJeqc7u65mRAjR-1eFKUfd&index=11

import time

def foo():
    return 1

def foo_1(a=True):
    return 1 if a else 10

def monkey_patch():
    return 10

def foo_3():
    time.sleep(30)
    return 1

def foo_test():
    return 1

DEBUG = True
if DEBUG:
    foo = foo_test

print(foo() == 1)
foo = monkey_patch
print(foo() == 10)


print(foo_1() == 1)
print(foo_1(False) == 10)




