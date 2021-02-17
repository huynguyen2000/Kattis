l, d, n = [int(i) for i in input().split()]
a = []
for _ in range(n):
  a.append(int(input()))
a.sort()
ret = 0
s = 6

for i in a:
  while i - s >= d:
    s += d
    ret += 1
  s = i + d
while s <= l - 6:
  s += d
  ret += 1
print(ret)
