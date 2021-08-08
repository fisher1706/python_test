from lesson22 import Rectangle, Square, Circle

rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)
print(rect1.get_area(),
      rect2.get_area())

sq1 = Square(5)
sq2 = Square(7)
print(sq1.get_area(),
      sq2.get_area())

cr1 = Circle(3)
cr2 = Circle(2)
print(cr1.get_area(),
      cr2.get_area())

figures = [rect1, rect2, sq1, sq2, cr1, cr2]
for figure in figures:
      print(figure, figure.get_area())






