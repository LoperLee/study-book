N, M = map(int, input().split())
graph, visit = dict(), set()
dist = [0 for _ in range(N+1)]
costList = [99999 for _ in range(N+1)]
answer, cost = 0, 0
for i in range(1, N+1):
    graph[i] = list()
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N+1):
    cost = 0
    queue = [i]
    visit.add(i)
    while queue:
        block = queue.pop(0)
        for col in graph[block]:
            if col not in visit:
                visit.add(col)
                dist[col-1] = dist[block-1]+1
                queue.append(col)
    costList[i] = 0
    for x in dist:
        costList[i] += x
    dist = [0 for _ in range(N+1)]
    visit = set()
    if costList[i] < costList[answer]:
        answer = i
print(answer)