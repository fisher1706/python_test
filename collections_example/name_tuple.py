from collections import namedtuple
import csv


"""
namedtuple - для создания структуры данных, среднее между типами и классом
"""


cat = namedtuple("cat", "name age color")
tom = cat("Tom", 25, "blue")


def work_with_csv_example(filename="points.csv"):
    Point = namedtuple("Point", "x y")

    with open(filename) as file:
        for line in csv.reader(file):
            point = Point._make(line)
            print(point)


if __name__ == "__main__":
    print(tom)
    print(tom[0])
    print(tom.age)
    print("*" * 200)

    work_with_csv_example()
