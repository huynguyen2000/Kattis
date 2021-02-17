n = int(input())
for i in range(n):
    s = int(input())
    a1 = [int(i) for i in input().split()]
    a2 = [int(i) for i in input().split()]
    a1.sort(reverse=True)
    a2.sort()
    ret = 0
    for j in range(s):
        ret += a1[j] * a2[j]
    print('Case #' + str(i+1) + ': ' + str(ret))
