s = input()
ind = 0
curr = ''
for i in range(len(s)):
    if s[i] == '{':
        if curr != '':
            print('  '*ind + curr)
        curr = ''
        print('  '*ind + '{')
        ind += 1
    elif s[i] == '}':
        if curr != '':
            print('  '*ind + curr)
        curr = ''
        ind -= 1
        if i + 1 < len(s) and s[i+1] == ',':
            curr = '}'
        else:
            print('  '*ind + '}')
    elif s[i] == ',':
        print('  '*ind + curr + ',')
        curr = ''
    else:
        curr += s[i]
if curr != '':
    print('  '*ind + curr)
