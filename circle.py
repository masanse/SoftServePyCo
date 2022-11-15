from math import pi
import figure


class Circle(figure.Figure):
    def __init__(self):
        figure.Figure.__init__(self)
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


def main():
    a = Circle()

    a.setting_side1(10)

    a.searching_area()
    print('Площа кола: ', a.getting_area())
    print('Радіус: ', a.getting_radius())


if __name__ == '__main__':
    main()
