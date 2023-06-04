import sys
import heapq
INF = 99999999

def dijkstra(graph, edge, start):
    table = [ INF ] * (edge + 1)
    table[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        dist, dest = heapq.heappop(queue)
        for new_dest, new_dist in graph[dest].items():
            total_dist = dist + new_dist
            if total_dist < table[new_dest]:
                table[new_dest] = total_dist
                heapq.heappush(queue, (total_dist, new_dest))
    return table

N, E = map(int, sys.stdin.readline().split(" "))
graph = { index: dict() for index in range(1, N+1) }
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split(" "))
    graph[A][B] = C
    graph[B][A] = C
v1, v2 = map(int, sys.stdin.readline().split(" "))

one = dijkstra(graph, N, 1)
two = dijkstra(graph, N, v1)
three = dijkstra(graph, N, v2)
minimum = min(one[v1] + two[v2] + three[N], one[v2] + three[v1] + two[N])
if minimum < INF:
    print(minimum)
else:
    print(-1)