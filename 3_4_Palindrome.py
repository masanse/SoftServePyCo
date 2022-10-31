s = input('Ану здивуй: ')
marks = '''_-&@#$%^ ,"'.`~ʼ!?:;’'''
new_s = ''

for i in s:
    if i not in marks:
        new_s += i.lower()

if new_s == new_s[::-1]:
    print('True')
else:
    print('False')
