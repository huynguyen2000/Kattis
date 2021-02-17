a, b = [int(i) for i in input().split()]

ret = []
if a < b:
    for i in range(1, b - a + 2):
        ret.append(a + i)
else:
    for i in range(1, a - b + 2):
        ret.append(b + i)

for i in ret:
    print(i)
