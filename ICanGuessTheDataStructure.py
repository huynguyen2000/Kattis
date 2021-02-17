from collections import deque
import heapq
from sys import stdin

tmp = 0

for line in stdin:

    if ' ' not in line:
        tmp = int(line)
        stack = []
        queue = deque()
        pqueue = []

        possible = [True, True, True]

    else:
        i, v = [int(i) for i in line.split()]

        if i == 1:
            stack.append(v)
            queue.append(v)
            heapq.heappush(pqueue, -1*v)
        else:
            try:
                if v != stack.pop(): possible[0] = False
                if v != queue.popleft(): possible[1] = False
                if v != -1 * heapq.heappop(pqueue): possible[2] = False
            except:
                possible = [False, False, False]
        
        tmp -= 1

        if tmp == 0:
            c = 0
            for j in possible:
                if j: c += 1

            if c == 1:
                for j in range(len(possible)):
                    if possible[j]:
                        if j == 0: print('stack')
                        if j == 1: print('queue')
                        if j == 2: print('priority queue')
            elif c == 0:
                print('impossible')
            else:
                print('not sure')
