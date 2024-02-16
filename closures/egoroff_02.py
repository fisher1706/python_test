# https://www.youtube.com/watch?v=TKv0c-Tyyuk&list=PLQAt0m1f9OHvv2wxPGSCWjgy1qER_FvB6&index=64

g = 'gray'

def colors(param='r'):
    y = 'yellow'
    g = 'green'

    def print_red():
        nonlocal y
        r = 'red'
        print(r, y, g)
        y = 'was changed'

    def print_blue():
        b = 'blue'
        print(b, y, g)

    if param == 'r':
        print_red()
    elif param == 'b':
        print_blue()
    else:
        print('zapel')


colors()



