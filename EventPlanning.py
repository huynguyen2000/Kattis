import math

n, b, h, w = [int(i) for i in input().split()]
min_price = b + 1
for i in range(h):
    p = int(input())
    la = [int(k) for k in input().split()]
    for j in la:
        if j >= n:
            min_price = min([min_price, n*p])
print(min_price if (min_price <= b) else 'stay home')
