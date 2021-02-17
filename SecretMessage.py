import math

def solve(msg):
    d = math.ceil(math.sqrt(len(msg)))
    msg += '*' * (d**2 - len(msg))
    data = []
    for i in range(d):
        temp = []
        for j in range(d):
            temp.append(msg[0])
            msg = msg[1:]
        data.append(temp)
    ret = ''
    for i in range(d):
        for j in range(d):
            if data[d-1-j][i] != '*':
                ret += data[d-1-j][i]
    print(ret)

    

c = int(input())
for i in range(c):
    msg = input()
    solve(msg)
