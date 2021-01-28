import sys
import heapq
INF = 10e6
V, E = map(int, sys.stdin.readline().split())
start_vert = int(sys.stdin.readline())
graph, dist = dict(), [ INF ] * (V+1)
for i in range(1, V+1):
    graph[i] = list()
for _ in range(E):
    vert, end, cost = map(int, sys.stdin.readline().split())
    graph[vert].append((end, cost))
# BFS
task = []
heapq.heappush(task, (0, start_vert))
dist[start_vert] = 0
while task:
    base, block = heapq.heappop(task)
    for vert, cost in graph[block]:
        cost = (base + cost)
        if cost < dist[vert]:
            dist[vert] = cost
            heapq.heappush(task, (cost, vert))
for i in range(1, V+1):
    answer = dist[i]
    if answer == INF:
        answer = "INF"
    print(answer)