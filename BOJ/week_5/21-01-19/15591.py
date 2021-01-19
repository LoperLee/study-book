import sys
from collections import deque
INF = 1e9 + 1
vert, neo = map(int, sys.stdin.readline().split())
graph = dict()
dist = [ [INF for _ in range(vert+1)] for _ in range(vert+1) ]
for _ in range(vert-1):
    A, B, usado = map(int, sys.stdin.readline().split())
    if A not in graph:
        graph[A] = list()
    if B not in graph:
        graph[B] = list()
    # 유사도 연결
    dist[A][B] = usado
    dist[B][A] = usado
    graph[A].append(B)
    graph[B].append(A)
# 미리 모든 간선을 계산해 둠
for i in range(1, vert+1):
    task, visit = deque([i]), {i}
    while task:
        watch = task.popleft()
        for j in graph[watch]:
            if j not in visit:
                dist[i][j] = min(dist[i][watch], dist[watch][j])
                visit.add(j)
                task.append(j)
# 입력값에 따른 동영상 추천 수
for i in range(neo):
    K, V = map(int, sys.stdin.readline().split())
    count = 0
    for i in dist[V]:
        if i < (1e9 + 1) and K <= i:
            count += 1
    print(count)