n = int(input())
a = [int(i)%2 for i in input().split()]
stack = []

for i in a:
    if len(stack) == 0:
        stack.append(i)
    else:
        if stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    
print(len(stack))
