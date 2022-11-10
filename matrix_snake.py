n, m = [int(input()) for _ in range(2)]

matrix = [[0 for i in range(m)] for j in range(n)]

i, j = 0, 0
for snake_number in range(1, n * m + 1):
    matrix[i][j] = snake_number
    if snake_number == n * m:
        break

    if j % 2 == 0 and i != n - 1:
        i += 1
    elif j % 2 == 0 and i == n - 1:
        j += 1
    elif j % 2 != 0 and i != 0:
        i -= 1
    elif j % 2 != 0 and i == 0:
        j += 1

for i in range(n):
    for j in range(m):
        print(f'{matrix[i][j]:3d}', end=' ')
    print()
