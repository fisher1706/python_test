# https://www.youtube.com/watch?v=7WSNq-T_xms&list=PLF4MWzDJPFSZJeqc7u65mRAjR-1eFKUfd&index=8

class A(object):
    x = 10

class B(A):
    pass

class C(A):
    pass

class D(C, B):
    pass

obj = D()
print(D.mro())