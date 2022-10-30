Lis = []
Lis += [int(_) for _ in input("Вкажіть послідовно п'ять чисел через пробіл: ").split()]
Lis = Lis[:5]
# print(Lis)

DictM = {'min': [0, 0], 'max': [Lis[0], 0]}

for i in range(len(Lis)):
    if DictM['max'][0] < Lis[i]:
        DictM['max'][0] = Lis[i]
        DictM['max'][1] = i + 1

DictM['min'][0] = DictM['max'][0]
DictM['min'][1] = DictM['max'][1]

for i in range(len(Lis)):
    if DictM['min'][0] > Lis[i]:
        DictM['min'][0] = Lis[i]
        DictM['min'][1] = i + 1

if DictM['max'][0] == DictM['min'][0]:
    print('Все рівно')
else:

    for i in range(len(Lis)):
        if DictM['max'][0] == Lis[i] and DictM['max'][1] != i + 1:
            DictM['max'] += [i + 1]

    for i in range(len(Lis)):
        if DictM['min'][0] == Lis[i] and DictM['min'][1] != i + 1:
            DictM['min'] += [i + 1]

    print('Максимум:', DictM['max'][0], 'Позиції: ', DictM['max'][1:])
    print('Мінімум:', DictM['min'][0], 'Позиції: ', DictM['min'][1:])
