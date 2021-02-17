def getrange(tree, i1, i2):
    return getsum(tree, i2) - getsum(tree, i1)

def getsum(tree, i): 
    s = 0
    i = i+1
    while i > 0: 
        s += tree[i] 
        i -= i & (-i) 
    return s 
  
def update(tree, n, i, v): 
    i += 1
    while i <= n: 
        tree[i] += v 
        i += i & (-i) 
  
def construct(arr, n): 
    tree = [0]*(n+1) 
    for i in range(n): 
        update(tree, n, i, arr[i])
    return tree 


n, k = [int(i) for i in input().split()]
mem = [0]*n
tree = construct(mem, n)

for _ in range(k):
    inp = input().split()

    if inp[0] == 'F':
        i = int(inp[1]) - 1
        mem[i] = int(not mem[i])
        if mem[i]: 
            update(tree, n, i, 1)
        else:
            update(tree, n, i, -1)
    else:
        i1, i2 = int(inp[1]) - 1, int(inp[2]) - 1
        ret = getrange(tree, i1, i2) + mem[i1]
        print(ret)
