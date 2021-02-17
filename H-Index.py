a = []
n = int(input())
for i in range(n):
    tmp = int(input())
    a.append(tmp)
a.sort()
i = 0
while len(a) != 0 and i < a[-1]:
    a.pop()
    i += 1
print(i)
