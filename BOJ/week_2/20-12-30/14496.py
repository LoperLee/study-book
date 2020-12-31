key, goal = map(int, input().split())
n, m = map(int, input().split())
graph = {}
visit = {}
dist = []
answer = -1
queue = []

for i in range(n):
    graph[i+1] = list()
    visit[i+1] = False
    dist.append(0)
for i in range(m):
    k, col = map(int, input().split())
    graph[k].append(col)
    graph[col].append(k)

queue.append(key)
visit[key] = True
if key != goal:
    while len(queue) > 0:
        block = queue.pop(0)
        for col in graph[block]:
            if not visit[col]:
                visit[col] = True
                dist[col-1] = dist[block-1]+1
                queue.append(col)
    print(dist[goal-1] <= 0 and -1 or dist[goal-1])
else:
    print(0)