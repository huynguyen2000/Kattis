inp = input()
data = []
while inp != '-1':
    splt = inp.split()
    temp_dict = {'time': int(splt[0]), 'prob': splt[1], 'res': splt[2]}
    data.append(temp_dict)
    inp = input()
    
seen = {}
score = 0
right = 0
for i in data:
    if i['res'] == 'right':
        right += 1
        score += i['time'] + 20*(seen[i['prob']] if i['prob'] in seen else 0)
    else:
        if i['prob'] in seen:
            seen[i['prob']] += 1
        else:
            seen[i['prob']] = 1
        
print(str(right) + ' ' + str(score))
