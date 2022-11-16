class Figure:
    def __init__(self):
        self.__angle1 = 0
        self.__angle2 = 0
        self.__side1 = 0
        self.__side2 = 0

    def getting_angle1(self):
        return self.__angle1

    def getting_angle2(self):
        return self.__angle2

    def getting_side1(self):
        return self.__side1

    def getting_side2(self):
        return self.__side2

    def setting_angle1(self, param):
        self.__angle1 = param

    def setting_angle2(self, param):
        self.__angle2 = param

    def setting_side1(self, param):
        self.__side1 = param

    def setting_side2(self, param):
        self.__side2 = param

    def __str__(self):
        return (f'Значення параметрів Figure на зараз:\nangle1 = {self.__angle1}\nangle2 = {self.__angle2}\n'
                f'side1 = {self.__side1}\nside2 = {self.__side2}')


def main():
    a = Figure()
    print(a)

    a.setting_side2(10)
    print(a)

    print(a.getting_angle1())


if __name__ == '__main__':
    main()
