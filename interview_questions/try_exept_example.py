# https://pyneng.readthedocs.io/ru/old_chapter_order/book/06_control_structures/6_exceptions.html

def func(a, b):
    try:
        print(a / b)
    except ZeroDivisionError as e:
        print(e)
    else:
        print('zapel')
    finally:
        print('close')


if __name__ == '__main__':
    func(5, 2)
