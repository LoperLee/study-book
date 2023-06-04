import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
elements = list(map(int, sys.stdin.readline().split()))

move_count = 0
rqueue = deque([ i for i in range(1, N+1) ])

for index in elements:
    while True:
        front = rqueue.popleft()
        if index == front:
            break
        move_count += 1
        if (front - index) >= 0:
            rqueue.appendleft(front)
            rqueue.appendleft(rqueue.pop())
        else:
            rqueue.append(front)

print(move_count)