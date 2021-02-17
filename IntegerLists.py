from collections import deque
n = int(input())
 
for _ in range(n):
    s = input()
    l = int(input())
    tmp = input()
    if l == 0:
        d = deque()
    else:
        d = deque([int(i) for i in tmp[1:-1].split(',')])
    
    o = False
    r = 0
    e = False
    for i in s:
        if i == 'R':
            o = not o
            r += 1
        else:
            if o:
                try:
                    d.pop()
                except:
                    print('error')
                    e = True
                    break
            else:
                try:
                    d.popleft()
                except:
                    print('error')
                    e = True
                    break
    if e:
        continue
    
    d = list(d)  
    if r % 2 == 1:
        d.reverse()
        
    print('[' + ','.join([str(i) for i in d]) + ']')
