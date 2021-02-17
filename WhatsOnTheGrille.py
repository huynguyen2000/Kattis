dim = int(input())
if dim < 1:
    print('invalid grille')
    exit(0)

coords = []
filled = [[False for i in range(dim)] for j in range(dim)]

try:
    for i in range(dim):
        s = input()
        for j in range(len(s)):
            if s[j] == '.':
                coords.append((i, j))
except:
    print('invalid grille')
    exit(0)

inp_tmp = input()
s_mes = [i for i in inp_tmp][::-1]

for j in range(4):
    for i in range(len(coords)):
        try:
            filled[coords[i][0]][coords[i][1]] = s_mes[-1]
            s_mes.pop()
            tmp = (coords[i][1], dim - 1 - coords[i][0])
            coords[i] = tmp
        except:
            print('invalid grille')
            exit(0)
    coords.sort()

ret = ''
for i in filled:
    try:
        ret += ''.join(i)
    except:
        print('invalid grille')
        exit(0)
print(ret)
