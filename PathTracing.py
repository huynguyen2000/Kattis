from sys import stdin

data = [['S']]
curr = {'x': 0, 'y': 0}
for i in stdin:
    i = i.rstrip()
    if i == 'down':
        curr['y'] += 1
        if curr['y'] > len(data) - 1:
            data += [[' '] * len(data[0])] 
        data[curr['y']][curr['x']] = 'S' if data[curr['y']][curr['x']] == 'S' else '*'
    elif i == 'up':
        if curr['y'] == 0:
            curr['y'] += 1
            data = [[' '] * len(data[0])] + data
        curr['y'] -= 1
        data[curr['y']][curr['x']] = 'S' if data[curr['y']][curr['x']] == 'S' else '*'
    elif i == 'right':
        curr['x'] += 1
        if curr['x'] > len(data[0]) - 1:
            for j in range(len(data)):
                data[j] += [' ']
        data[curr['y']][curr['x']] = 'S' if data[curr['y']][curr['x']] == 'S' else '*'
    elif i == 'left':
        if curr['x'] == 0:
            curr['x'] += 1
            for j in range(len(data)):
                data[j] = [' '] + data[j]
        curr['x'] -= 1
        data[curr['y']][curr['x']] = 'S' if data[curr['y']][curr['x']] == 'S' else '*'
    elif i == 'q':
        break

    # for k in data:
    #     print(''.join(k))

data[curr['y']][curr['x']] = 'E'
for j in range(len(data)):
    data[j] = ['#'] + data[j] + ['#']
data = [['#'] * len(data[0])] + data + [['#'] * len(data[0])]

for k in data:
    print(''.join(k))
