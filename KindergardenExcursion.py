s = input()
c = 0
seen = [0, 0, 0]
seen[int(s[0])] += 1
for i in range(1, len(s)):
    c += sum(seen[int(s[i])+1:])
    seen[int(s[i])] += 1
print(c)
