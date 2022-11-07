print('\nРівняння має вигляд: a•x²+b•x+c=0\n')


def input_data():
    arg = []
    arg += [float(_) for _ in input('Вкажіть послідовно значення аргументів a,b,c через пробіл:').split()]
    return arg


def solve_equation(a: float, b: float, c: float):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        print('Дискримінант =', discriminant, ",від'ємний, тому у відповіді комплексні числа")
    else:
        print('Дискримінант =', discriminant)

    if discriminant == 0:
        x = -b / (2 * a)
        print('x = ', x)
    else:
        x1 = (-b + discriminant ** (1 / 2)) / (2 * a)
        x2 = (-b - discriminant ** (1 / 2)) / (2 * a)
        print(f'x1 = {x1}\nx2 = {x2}')


arg = input_data()

if len(arg) == 3:
    solve_equation(*arg)
elif len(arg) == 0:
    solve_equation(6, 5, 8)
else:
    print('Щось пішло не так')
