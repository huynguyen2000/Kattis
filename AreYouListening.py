import math
cx, cy, n = [int(i) for i in input().split()]
data = []
for _ in range(n):
    x, y, r = [int(i) for i in input().split()]
    d = math.sqrt((cx - x)**2 + (cy - y)**2) - r
    data.append(d if d > 0 else 0)
data.sort()
print(math.floor(data[2]))
