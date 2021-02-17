n = int(input())
for _ in range(n):
    ns = int(input())
    segs = input().split()
    blue = []
    red = []
    for i in segs:
        if i[-1] == 'B':
            blue.append(i)
        else:
            red.append(i)
    blue.sort(key=lambda x : int(x[:-1]))
    red.sort(key=lambda x : int(x[:-1]))
    num_ele = min([len(blue), len(red)])
    ret = 0
    for i in range(num_ele):
        ret += int(blue[len(blue) - 1 - i][:-1]) + int(red[len(red) - 1 - i][:-1])
    ret -= num_ele*2
    print('Case #' + str(_+1) + ': ' + str(ret))
