import math

n, k = [int(i) for i in input().split()]
c = []
max_ct = -1
for i in range(n):
    t = int(input())
    while (len(c) != 0) and (c[0] + 1000 <= t):
        c.pop(0)
    c.append(t)
    max_ct = max([max_ct, math.ceil(len(c) / k)])
print(max_ct)   
