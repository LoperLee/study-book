import sys
N, M = map(int, sys.stdin.readline().split())
queue, mapper = list(), dict()
count = 0
for _ in range(M):
    num = sys.stdin.readline().rstrip()
    queue.append(num)
    mapper[num] = len(queue)-1
for i in range(len(queue)):
    if count >= N:
        break
    if i != mapper[queue[i]]:
        continue
    print(queue[i])
    count += 1