l, n = [int(i) for i in input().split()]
a = [0] + [int(i) for i in input().split()] + [l]
ret = []

for i in range(1, len(a)):
    for j in range(i):
        ret.append(a[i] - a[j])

ret.sort()

print(' '.join([str(i) for i in list(set(ret))]))
