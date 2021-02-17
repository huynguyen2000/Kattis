x, y = [int(i) for i in input().split()]
print('possible' if (4*x + 3*y) % 2 == 0 else 'impossible')
