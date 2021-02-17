n = int(input())
data = {}
for _ in range(n):
    a = ''.join([str(i) for i in sorted([int(i) for i in input().split()])])
    if a in data:
        data[a] += 1
    else:
        data[a] = 1
mx_ct = max(data.values())
ret = 0
for i in data.values():
    if i == mx_ct:
        ret += i
print(ret)
