class Shape:
    width = 5
    height = 5
    printChar = '#'


    def print_row(self, i):
        raise NotImplementedError("Will be implemented by children extending this class")


    def print(self):
        for i in range(self.height):
            self.print_row(i)



class Square(Shape):
    def print_row(self, i):
        print(self.printChar * self.width)


class Triangle(Shape):
    height = 5
    width = 2 * height

    # def print_row(self, i):
    #     print(self.printChar * (i + 1))
    #
    def print_row(self, i):
        triangle_width = i * 2 + 1
        padding = int(self.width - triangle_width / 2)
        print(" " * padding + self.printChar * triangle_width)


if __name__ == '__main__':
    s = Square()
    s.print()

    t = Triangle()
    t.print()
