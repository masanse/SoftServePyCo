from math import pi
import tkinter
import figure


class Circle(figure.Figure):
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
        canv = tkinter.Canvas(root, width=1024, height=800, bg='black')

        def drawing_by_click(event):
            x = event.x
            y = event.y
            circ = canv.create_oval(x, y, x + self.__radius, y + self.__radius, fill='red')
            return circ

        canv.bind('<Button-1>', drawing_by_click)
        canv.pack()
        root.mainloop()


def main():
    a = Circle()

    a.setting_side1(500)

    a.searching_area()
    print('Площа кола: ', a.getting_area())
    print('Радіус: ', a.getting_radius())

    # a._Figure__side1 = 5
    # print(a)

    a.drawing_circle()

    # for i in dir(a):
    #     print(i)


if __name__ == '__main__':
    main()
