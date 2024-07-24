# https://www.youtube.com/watch?v=6H_kC9PYhus&list=PLhqLR-FtmNaXXnYQ7tsy2Fw7USL14fdfB&index=5

def count_deaf_rats(town: str) -> int:
    count = town.replace(" ", "")[::2].count("O")
    return count


if __name__ == '__main__':
    data = "~O ~O ~O ~O O~ O~P"
    x = count_deaf_rats(data)
    print(x)

    print(data.replace(" ", "")[::2])
