try:
    a = int(input('Ввести код елементу: '))
    print(chr(a))
except ValueError:
    print('Шото не то')