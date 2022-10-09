import sys
N = int(sys.stdin.readline())
cost = [[0, 0, 0]]
for _ in range(N):
    cost.append(list(map(int, sys.stdin.readline().split())))
for i in range(1, N+1):
    for j in range(3):
        cos = 0
        if j == 0:
            cos = cost[i-1][2]
            if cost[i-1][1] < cost[i-1][2]:
                cos = cost[i-1][1]
        elif j == 1:
            cos = cost[i-1][2]
            if cost[i-1][0] < cost[i-1][2]:
                cos = cost[i-1][0]
        elif j == 2:
            cos = cost[i-1][1]
            if cost[i-1][0] < cost[i-1][1]:
                cos = cost[i-1][0]
        cost[i][j] += cos
answer = cost[N][0]
for i in range(1, 3):
    if cost[N][i] < answer:
        answer = cost[N][i]
print(answer)