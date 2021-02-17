N, t = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

if t == 1:
    print('7')
elif t == 2:
    if A[0] > A[1]:
        print('Bigger')
    elif A[0] == A[1]:
        print('Equal')
    else:
        print('Smaller')
elif t == 3:
    temp = [A[0], A[1], A[2]]
    temp.sort()
    print(temp[1])
elif t == 4:
    print(sum(A))
elif t == 5:
    print(sum([i for i in A if i % 2 == 0]))
elif t == 6:
    print(''.join([chr(97+i % 26) for i in A]))
elif t == 7:
    temp = [0 for i in range(N)]
    i = 0
    while True:
        if (i < 0) or (i > N - 1):
            print('Out')
            break
        elif i == N - 1:
            print('Done')
            break
        elif temp[i] == 1:
            print('Cyclic')
            break
        temp[i] = 1
        i = A[i]
