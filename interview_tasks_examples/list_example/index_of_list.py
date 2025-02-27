"""
Срезы в Python — это «синтаксический сахар» для более короткой и понятной записи работы со строками и массивами,
который позволяет записывать многие операции со строками и массивами более «красиво»,
например:

s = “my super string” print(s[::-1]) # этот «срез» развернёт строку в обратную сторону

print(s[:4]) # этот «срез» вернёт первые четыре символа из строки

print(s[-5:]) # этот «срез» вернёт последние пять символов из строки

sequence[start:end:step]
"""

data = [1, 2, 3, 4, 5, 6, 7]
# s = slice(0, 5, 1)
s = slice(0, 5, 2)


if __name__ == "__main__":
    print(data[1:4])
    print(data[-3:])
    print(data[:-1])
    print("*" * 200)
    print(data[::-1])
    print(data[:])
    print("*" * 200)

    print(data[s])
