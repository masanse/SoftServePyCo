n = int(input('Вкажіть розмір матриці: '))
matrix = [[0 for i in range(n)] for j in range(n)]
i, j = 0, 0
for snail_number in range(1, n ** 2 + 1):
    matrix[i][j] = snail_number
    if snail_number == n ** 2:
        break

    if i <= j + 1 and i + j < n - 1:
        j += 1
    elif i < j and i + j >= n - 1:
        i += 1
    elif i >= j and i + j > n - 1:
        j -= 1
    elif i > j and i + j <= n - 1:
        i -= 1

for i in range(n):
    for j in range(n):
        print(f'{matrix[i][j]:3d}', end=' ')
    print()
