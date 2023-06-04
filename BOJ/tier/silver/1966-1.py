import sys
from collections import deque

def calc_position(position, length):
    ret = position - 1
    if ret < 0:
        return length - 1
    return ret

K = int(sys.stdin.readline())

for _ in range(K):
    answer = 0
    N, M = map(int, sys.stdin.readline().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    while queue:
        now = queue.popleft()
        over_now = 0 if len(queue) <= 0 else max(queue)
        if now < over_now:
            queue.append(now)
            M = calc_position(M, len(queue))
        else:
            answer += 1
            if M == 0:
                break
            M = calc_position(M, len(queue))
    print(answer)