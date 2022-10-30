print('\nРівняння має вигляд: a•x²+b•x+c=0\n')


def quadr_solution(a, b, c):
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


arg = []
arg += [float(_) for _ in input('Вкажіть послідовно значення аргументів a,b,c через пробіл:\n').split()]

if len(arg) == 3:
    quadr_solution(*arg)
elif len(arg) == 0:
    quadr_solution(6, 5, 8)
else:
    print('Щось пішло не так')
