n = int(input())
c = 0
for i in range(n):
    s = input()
    if s.find('CD') == -1:
        c += 1

print(c)
