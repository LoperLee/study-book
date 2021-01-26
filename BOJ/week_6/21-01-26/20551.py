import sys
N, M = map(int, sys.stdin.readline().split())
numbers, table = list(), dict()
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))
numbers.sort()
for i in range(N):
    if numbers[i] not in table:
        table[numbers[i]] = i
for _ in range(M):
    question = int(sys.stdin.readline())
    if question not in table:
        print(-1)
    else:
        print(table[question])