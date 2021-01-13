import sys
from collections import deque
while True:
    N = int(sys.stdin.readline())
    answer = ""
    if N == 0:
        break
    task, used = deque(["1"]), {"1"}
    while task:
        now = task.popleft()
        if int(now) % N == 0:
            answer = now
            break
        left, right = '{}0'.format(now), '{}1'.format(now)
        if left not in used:
            task.append(left)
        if right not in used:
            task.append(right)
    print(answer)