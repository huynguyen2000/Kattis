from collections import deque

n, s = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

if s == 1:
    a =set(a)
    for i in range(7777):
        if i in a and 7777 - i in a:
            print('Yes')
            exit(0)
    print('No')
elif s == 2:
    if len(a) == len(set(a)):
        print('Unique')
    else:
        print('Contains Duplicate')
elif s == 3:
    c = 1
    curr = -1
    a.sort()
    for i in a:
        if i != curr:
            curr = i
            c = 1
        else:
            c += 1
            if c > n // 2:
                print(curr)
                exit(0)
    print(-1)
elif s == 4:
    a.sort()
    if n % 2 == 1:
        print(a[n//2])
    else:
        print(a[n//2 - 1], a[n//2])
elif s == 5:
    a.sort()
    d = deque(a)
    while d[0] < 100:
        d.popleft()
    while d[-1] > 999:
        d.pop()
    print(' '.join([str(i) for i in list(d)]))
