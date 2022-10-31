s1, s2 = input('Стрінга 1: '), input('Стрінга 2: ')

if len(s1) == len(s2):
    for i in range(len(s1)):
        if i == (len(s1) - 1) and s1[i] == s2[i]:
            print('True')

        if s1[i] == s2[i]:
            continue
        else:
            print('False')
            break

else:
    print('False')