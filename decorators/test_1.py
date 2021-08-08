# https://www.youtube.com/watch?v=Va-ovLxHmus&list=PLQAt0m1f9OHvv2wxPGSCWjgy1qER_FvB6&index=67

def decorator(func):
    def inner(*args, **kwargs):
        print('start decorator')
        func(*args, **kwargs)
        print('finish decorator')
    return inner

def header(func):
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('<h1>')
    return inner

def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('<table>')
    return inner

@header  # say = header(say)
@table  # say = table(header(say))
def say(name):
    print('hello', name)

def buy():
    print('buy world')

# buy = decorator(buy)
# buy()

# d = decorator(say)
# print(d)
# d()


# say = decorator(say)
# print(say)
# say('oleg')


say('oleg')

