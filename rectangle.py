from figure import Figure


class Rectangle(Figure):
    def __init__(self):
        super().__init__()
        self.__side3 = 0
        self.__side4 = 0
        self.__angle3 = 0
        self.__angle4 = 360 - self.__angle3 - self.getting_angle2() - self.getting_angle1()

    def setting_side3(self, param):
        self.__side3 = param

    def setting_side4(self, param):
        self.__side4 = param

    def setting_angle3(self, param):
        self.__angle3 = param

    def getting_side3(self):
        return self.__side3

    def getting_side4(self):
        return self.__side4

    def getting_angle3(self):
        return self.__angle3

    def getting_angle4(self):
        return self.__angle4

    def searching_perimetr(self):
        return self.__side4 + self.__side3 + self.getting_side1() + self.getting_side2()

    def __str__(self):
        return (f'Значення параметрів Circle на зараз:\n'
                f'side1 = {self.getting_side1()}\n'
                f'side2 = {self.getting_side2()}\n'
                f'side3 = {self.getting_side3()}\n'
                f'side4 = {self.getting_side2()}\n')



def main():
    w = Rectangle()
    r = Rectangle()
    r.setting_side1(10)
    r.setting_side2(15)
    r.setting_side3(17)
    r.setting_side4(19)
    print(r.searching_perimetr())

    print(f'Кількість екземплярів {Rectangle.counting(Figure)}')


if __name__ == '__main__':
    main()
