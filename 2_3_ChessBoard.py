a = chr(9633)
b = chr(9632)
x = int(input('Кількість строк: '))
y = int(input('Кількість стовбчиків: '))


d = [['*' for j in range(y)] for i in range(x)]
for i in range(x):
    for j in range(y):
        if (i % 2 != 0 and j % 2 == 0) or (i % 2 == 0 and j % 2 !=0):
            d[i][j] = a
        else:
            d[i][j] = b

for i in range(x):
    print(*d[i])
