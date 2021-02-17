import sys

data = {}

for line in sys.stdin:
    line = line.split()
    if line[0] == 'group':
        data[line[1]] = set(line[3:])
    else: 
        line.reverse()   
        i = 0
        while len(line) > i:
            if line[i] in ('union', 'intersection', 'difference'):
                if line[i] == 'union':
                    line[i] = line[i-1].union(line[i-2])
                elif line[i] == 'intersection':
                    line[i] = line[i-1].intersection(line[i-2])
                elif line[i] == 'difference':
                    line[i] = line[i-1].difference(line[i-2])
                else:
                    print('error')
                    exit(0) 
                i -= 1
                line.pop(i)
                line.pop(i-1)

            else:
                line[i] = data[line[i]]
                i += 1
        print(' '.join(sorted(line[0])))
