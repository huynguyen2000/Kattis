ntests = int(input())
for _ in range(ntests):
    td, tm = [int(i) for i in input().split()]
    daysinmonth = [int(i) for i in input().split()]
    ret = 0
    start = 1
    for i in daysinmonth:
        if start == 1 and i > 12:
            ret += 1
        start = ((i % 7) + start) % 7
        start = 7 if start == 0 else start

    print(ret)
