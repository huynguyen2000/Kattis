ntests = int(input())
for _ in range(ntests):
    npizzas = int(input())
    frgn_l = set()
    engl_l = set()
    frgn_d = {}
    engl_d = {}
    for j in range(npizzas):
        name = input()
        tmp = input().split()[1:]
        for i in tmp:
            frgn_l.add(i)
            if i not in frgn_d.keys():
                frgn_d[i] = name
            else:
                frgn_d[i] += name
        tmp = input().split()[1:]
        for i in tmp:
            engl_l.add(i)
            if i not in engl_d.keys():
                engl_d[i] = name
            else:
                engl_d[i] += name
                
    frgn_l = sorted(list(frgn_l))
    engl_l = sorted(list(engl_l))

    for i in frgn_l:
        for j in engl_l:
            if frgn_d[i] == engl_d[j]:
                print('(' + i + ', ' + j + ')')
