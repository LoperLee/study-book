from collections import deque
INF = 10e6
K, N, R = int(input()), int(input()), int(input())
graph, table = dict(), [ INF ] * (N+1)
# 초기화
for i in range(1, N+1):
    graph[i] = list()
for _ in range(R):
    start, end, length, cost = map(int, input().split())
    graph[start].append((end, length, cost))
print(graph)
# BFS로 풀어보기
task = deque([(0, 1, 0)])
# heapq.heappush(task, (0, 1, 0)) # cost, vert, len
table[1] = 0
while task:
    # cost, vert, length = map(int, heapq.heappop(task))
    cost, vert, length = map(int, task.popleft())
    print((cost, vert, length), table)
    for in_end, in_length, in_cost in graph[vert]:
        # cost, vert, length
        obj = (cost + in_cost, in_end, length + in_length)
        print("inner", obj)
        if obj[0] > K:
            continue
        print("inner2", obj)
        if obj[2] < table[in_end]:
            # heapq.heappush(task, obj)
            task.append(obj)
            table[in_end] = obj[2]
print(table[N])