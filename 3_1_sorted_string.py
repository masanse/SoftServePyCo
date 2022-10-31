abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = '0123456789'
a = input('Дай стрінгу: ')
a1, a2, a3 = '', '', ''
for i in a:
    if i in num:
        a1 += i
    if i in abc:
        a2 += i
    if i not in abc and i not in num and i != ' ':
        a3 += i

print(*sorted(a1), *sorted(a2), *sorted(a3))
