import heapq
import sys

N = int(sys.stdin.readline())
queue = []
for _ in range(N):
    M = int(sys.stdin.readline())
    if M == 0:
        if len(queue) <= 0:
            sys.stdout.write("0\n")
        else:
            value = heapq.heappop(queue)
            sys.stdout.write(f"{str(value[0] * value[1])}\n")
    else:
        value = (M, 1)
        if M < 0: value = (M * -1, -1)
        heapq.heappush(queue, value)