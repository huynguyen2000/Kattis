n = int(input())
l1 = input()
l2 = input()

if n % 2 == 1:
    for i in range(len(l1)):
        if l1[i] == l2[i]:
            print('Deletion failed')
            exit(0)
    print('Deletion succeeded')
else:
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            print('Deletion failed')
            exit(0)
    print('Deletion succeeded')
