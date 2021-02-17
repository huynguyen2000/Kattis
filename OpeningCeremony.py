n = int(input())
a = sorted([int(i) for i in input().split() if i != '0'])
ret = n
for i in range(n):
    ret = min([ret, n-i-1 + a[i]])
print(ret)
