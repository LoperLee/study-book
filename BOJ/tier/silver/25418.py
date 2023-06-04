import sys
from collections import deque

A, K = map(int, sys.stdin.readline().split())

queue = deque([(A + 1, 1), (A * 2, 1)])
while queue:
    pointer = queue.popleft()
    A1 = pointer[0] + 1
    A2 = pointer[0] * 2
    if A1 < K:
        queue.append((A1, pointer[1] + 1))
    if A2 < K:
        queue.append((A2, pointer[1] + 1))
    if A1 == K or A2 == K:
        print(pointer[1] + 1)
        break