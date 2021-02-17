def find_root(arr, r):
    while r != arr[r]:
        r = arr[r]
    return r

def merge(arr, num, r1, r2):
    r1 = find_root(arr, r1)
    r2 = find_root(arr, r2)

    if r1 != r2:
        num[r1] += num[r2]
        num[r2] = 0
        arr[r2] = r1

parent = [i for i in range(500001)]
set_size = [1 for i in range(500001)]
ret = 0

n = int(input())
for _ in range(n):
    inp = [int(i) for i in input().split()]
    ni = inp[0]
    vi = inp[1:]

    # find the root of each set encompassing the ingredients
    uvi = set()
    for i in vi:
        uvi.add(find_root(parent, i))

    # checks if all ingredients are in indiviual sets
    count = 0
    for i in uvi:
        count += set_size[i]
    
    # fails if ingredient is found in more than 1 sets, size would be higher
    # if succeed, merge all ingredients into 1 aet
    if count == ni:
        ret += 1
        for i in vi:
            merge(parent, set_size, vi[0], i)

print(ret)
