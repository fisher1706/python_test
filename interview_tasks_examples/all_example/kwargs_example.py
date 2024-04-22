def total_marks(**kwargs):
    total = 0
    for marks in kwargs.values():
        total += marks
    return total


if __name__ == '__main__':
    print(total_marks(maths=80, science=90, english=80))
    