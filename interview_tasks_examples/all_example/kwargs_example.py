def total_marks(**kwargs):
    total = 0
    for marks in kwargs.values():
        total += marks
    return total


def total_marks_comp(**kwargs):
    return sum([marks for marks in kwargs.values()])




if __name__ == "__main__":
    print(total_marks(maths=80, science=90, english=80))
    print("*" * 200)
    print(total_marks_comp(maths=80, science=90, english=80))
