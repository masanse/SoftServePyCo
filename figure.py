class Figure:
    __count = 0

    def __init__(self):
        Figure.__count += 1
        self.__angle1 = 0
        self.__angle2 = 0
        self.__side1 = 0
        self.__side2 = 0

    def __del__(self):
        Figure.__count -= 1
    def getting_angle1(self):
        return self.__angle1

    def getting_angle2(self):
        return self.__angle2

    def getting_side1(self):
        return self.__side1

    def getting_side2(self):
        return self.__side2

    def counting(self):
        return Figure.__count

    def setting_angle1(self, param):
        self.__angle1 = param

    def setting_angle2(self, param):
        self.__angle2 = param

    def setting_side1(self, param):
        self.__side1 = param

    def setting_side2(self, param):
        self.__side2 = param

    def __str__(self):
        return 'Метод неперевизначен'


# def main():
#     a = Figure()
#     b = Figure()
#
#     # print(a)
#
#     a.setting_side2(10)
#     # print(a)
#
#     # print(a.getting_angle1())
#
#
if __name__ == '__main__':
#     main()
    c = Figure()
    d = Figure()

    print(Figure.counting(Figure))
