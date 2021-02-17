c = int(input())
a = [int(i) for i in input().split()]

lmax = [0]
rmin = [2147483647]

for i in range(len(a) - 1):
    lmax.append(max([lmax[-1], a[i]]))
for i in range(len(a) - 1, 0, -1):
    rmin.append(min([rmin[-1], a[i]]))

rmin.reverse()
ret = 0

for i in range(len(a)):
    if lmax[i] < a[i] < rmin[i]:
        ret += 1

print(ret)
