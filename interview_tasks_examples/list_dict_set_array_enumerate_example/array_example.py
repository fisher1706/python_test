from pprint import pprint


def approach_one(matrix, rows, cols):
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        matrix.append(row)
    pprint(matrix)


def approach_two(rows, cols):
    matrix = [[0 for _ in range(rows)] for _ in range(cols)]
    pprint(matrix)


if __name__ == "__main__":
    m = []
    rs = 5
    cs = 5

    approach_one(m, rs, cs)
    approach_two(rs, cs)
