s = input()
d = []

for i in s:
    if i == '<':
        d.pop()
    else:
        d.append(i)

print(''.join(d))
