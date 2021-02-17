from collections import deque

for _ in range(int(input())):
    data = []
    mx_ct = -1
    for __ in range(int(input())):
        s = input().split()
        tmp = s[1].split('-')
        tmp.reverse()
        for i in range(len(tmp)):
            if tmp[i] == 'upper':
                tmp[i] = '1'
            elif tmp[i] == 'middle':
                tmp[i] = '2'
            if tmp[i] == 'lower':
                tmp[i] = '3'
        mx_ct = max([mx_ct, len(tmp)])
        data.append([tmp, s[0][:-1]])

    for i in range(len(data)):
        while len(data[i][0]) < mx_ct:
            data[i][0].append('2')
        data[i][0] = int(''.join(data[i][0]))
        data[i] = tuple(data[i])

    data.sort()

    for i in data:
        print(i[1])
    print('='*30)
