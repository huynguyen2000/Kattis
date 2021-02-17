c = int(input())
l = [int(i) for i in input().split()]
l.sort()
data = [[l[0]]]
for i in range(1, c):
    if l[i] == data[-1][-1] + 1:
        data[-1].append(l[i])
    else:
        data.append([l[i]])
ret = []
for i in data:
    if len(i) == 1:
        ret.append(str(i[0]))
    elif len(i) == 2:
        ret.append(str(i[0]) + ' ' + str(i[-1]))
    else:
        ret.append(str(i[0]) + '-' + str(i[-1]))
print(' '.join(ret))
