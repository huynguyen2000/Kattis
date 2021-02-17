n, m = [int(i) for i in input().split()]
parent = [i for i in range(n)]
bal = []
rels = []
for i in range(n):
    bal.append(int(input()))

if m == 0:
    print('IMPOSSIBLE')
    exit(0)

for i in range(m):
    r1, r2 = [int(i) for i in input().split()]
    rels.append([r1, r2])
    while r1 != parent[r1]:
        r1 = parent[r1]
    while r2 != parent[r2]:
        r2 = parent[r2]
    parent[r2] = r1

for i in range(n):
    head = i
    while head != parent[head]:
        head = parent[head]
    if head != i:
        bal[head] += bal[i]
        bal[i] = 0

for i in bal:
    if i != 0:
        print('IMPOSSIBLE')
        exit(0)
print('POSSIBLE')
