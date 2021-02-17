import sys

data = {}
for line in sys.stdin:
    line = line.split()
    if line[0] == 'def':
        data[line[1]] = int(line[2])
    elif line[0] == 'calc':
        try:
            ret = data[line[1]]
            op = True
            for i in range(2, len(line) - 1):
                if line[i] == '-':
                    op = False
                elif line[i] == '+':
                    op = True
                else:
                    if op:
                        ret += data[line[i]]
                    else:
                        ret -= data[line[i]]
            name = list(data.keys())[list(data.values()).index(ret)]
            print(' '.join(line[1:]) + ' ' + name)
                    
        except:
            print(' '.join(line[1:]) + ' unknown')
            
    else:
        data = {}
