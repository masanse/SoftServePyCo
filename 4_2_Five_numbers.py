
def input_data():
    '''Вхідні дані'''
    list_in = [int(_) for _ in input("Вкажіть послідовно п'ять чисел через пробіл: ").split()]
    return list_in[:5]  


def search_mm(l: list):
    '''Пошук мінімума та максимума та їх позицій в рядку'''
    a = min(l)
    b = max(l)
    lmin, lmax = [], []
    for i in range(len(l)):
        if l[i] == a:
            lmin += [i]
        if l[i] == b:
            lmax += [i]

    return f'minimum: {a}, position: {lmin}\nmaximum: {b}, position {lmax}'


print(search_mm(input_data()))
