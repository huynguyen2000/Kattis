import datetime

l1 = [int(i) for i in input().split(':')]
x = datetime.timedelta(hours=l1[0], minutes=l1[1], seconds=l1[2])
l2 = [int(i) for i in input().split(':')]
y = datetime.timedelta(hours=l2[0], minutes=l2[1], seconds=l2[2])
ret = str(y - x).split(' ')[-1]
if ret == '0:00:00':
    print('24:00:00')
else:
    print(('0' if len(ret) == 7 else '') + ret)
