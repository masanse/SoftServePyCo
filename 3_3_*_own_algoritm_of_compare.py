s1, s2 = input('Стрінга 1: '), input('Стрінга 2: ')
checklist = []
positions = []

if len(s1) == len(s2):
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            checklist.append(0)
        else:
            checklist.append(1)

    for i in range(len(checklist)):
        if checklist[i] != 0:
            positions.append(i+1)

    if positions == []:
        print('True')
    else:
        print(f'False бо не співпадають позиції: {positions}')

else:
    print('False бо різна кількість елементів')
