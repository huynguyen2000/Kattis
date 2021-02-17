c = int(input())
l = [{'val': int(v), 'id': i+1} for i, v in enumerate(input().split())]

curr_chair = 0
curr_num = l[curr_chair]['val']
while len(l) != 1:
    curr_chair = (curr_chair + (curr_num - 1)) % len(l)
    l.pop(curr_chair)
    curr_chair = (curr_chair) % len(l)
    curr_num = l[curr_chair]['val']
print(l[0]['id'])
