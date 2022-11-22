from math import pi
import tkinter
from figure import Figure


class Circle(Figure):
    def __init__(self):
        super().__init__()
        self.__radius = 0
        self.__area = 0

    def setting_radius(self, param):
        self.__radius = param

    def setting_area(self, param):
        self.__area = param

    def getting_radius(self):
        return self.__radius

    def getting_area(self):
        return self.__area

    def searching_radius(self):
        side = Circle.getting_side1(self)
        if side > 0 and self.__radius == 0:
            self.__radius = side / (2 * pi)

    def searching_area(self):
        Circle.searching_radius(self)
        if self.__radius >= 0:
            self.__area = pi * self.__radius ** 2

    def drawing_circle(self):
        Circle.searching_radius(self)
        root = tkinter.Tk()
        canv = tkinter.Canvas(root, width=1920, height=1080, bg='black')

        def drawing_by_click(event):
            x = event.x
            y = event.y
            circ = canv.create_oval(x, y, x + self.__radius, y + self.__radius, fill='red')
            return circ

        canv.bind('<Button-1>', drawing_by_click)
        canv.pack()
        root.mainloop()

    def __str__(self):
        return (f'Значення параметрів Circle на зараз:\n'
                f'angle1 = {Circle.getting_angle1(self)}\n'
                f'angle2 = {Circle.getting_angle2(self)}\n'
                f'side1 = {Circle.getting_side1(self)}\n'
                f'side2 = {Circle.getting_side2(self)}\n'
                f'radius = {Circle.searching_radius(self)}')


def main():
    a = Circle()
    b = Circle()
    c = Circle()
    c.setting_side1(1500)
    print(c)
    del (b)

    a.setting_side1(1000)

    a.searching_area()
    print('Площа кола: ', a.getting_area())
    print('Радіус: ', a.getting_radius())

    print(f'Кількість екземплярів {Circle.counting(Figure)}')

    c.drawing_circle()


if __name__ == '__main__':
    main()
