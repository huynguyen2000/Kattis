n, m = [int(i) for i in input().split()]
sizes = []
need = []
for _ in range(n):
    sizes.append(int(input()))
for _ in range(m):
    need.append(int(input()))
sizes.sort()
ret = 0
for i in need:
    for j in sizes:
        if j >= i:
            ret += j - i
            break
print(ret)
