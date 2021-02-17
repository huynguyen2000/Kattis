import math
b, k, g = [int(i) for i in input().split()]
print(math.ceil((b - 1) / (k // g)))
