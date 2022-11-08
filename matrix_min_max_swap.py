from random import randint


def input_matrix_size() -> tuple:
    y = input('кількість стовбчиків: ')
    if y == 'exit': raise SystemExit

    x = input('кількість строк: ')
    try:
        if int(x) > 0 and int(y) > 0:
            return int(y), int(x)
        else:
            print("Потрібно ввести дані в форматі integer та більше нуля, для виходу введіть exit")
            return input_matrix_size()
    except ValueError:
        print("Потрібно ввести дані в форматі integer та більше нуля, для виходу введіть exit")
        return input_matrix_size()


def matrix_creating_karkas(xy: tuple) -> list:
    matrix = [[0 for i in range(xy[0])] for j in range(xy[1])]
    return matrix


def matrix_filling(matrix: list) -> list:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = randint(1, len(matrix) * len(matrix[0]) * 10)
    return matrix


def matrix_showing(matrix: list) -> None:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f'{matrix[i][j]:8d}', end=' ')
        print('')
    print('')


def searching_minmax(matrix: list) -> tuple:
    min = matrix[0][0]
    position_min = 0
    max = matrix[0][0]
    position_max = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max:
                max = matrix[i][j]
                position_max = j
            if matrix[i][j] < min:
                min = matrix[i][j]
                position_min = j
    print(f'minimum = {min}\nmaximum = {max}\n')
    return min, position_min, max, position_max


def matrix_replace(matrix: list, t: tuple) -> list:
    lminmax = [[], []]
    for i in range(len(matrix)):
        lminmax[0] += [matrix[i][t[1]]]
        lminmax[1] += [matrix[i][t[3]]]
    for i in range(len(matrix)):
        matrix[i][t[1]] = lminmax[1][i]
        matrix[i][t[3]] = lminmax[0][i]
    return matrix


def saving_in_file(t:tuple):
    outfile = open('result.txt', 'w')
    outfile.write(f'minimum = {t[0]}\nmaximum = {t[2]}\n')
    outfile.close()



karkas = matrix_creating_karkas(input_matrix_size())
matrix_showing(karkas)

matrix = matrix_filling(karkas)
matrix_showing(matrix)

result = searching_minmax(matrix)

matrix_r = matrix_replace(matrix, result)
matrix_showing(matrix_r)

saving_in_file(result)
