import sys
n, m = map(int, sys.stdin.readline().split())
graph = dict()
visit = set()
answer = 0
def dfs(start):
    global graph, visit
    visit.add(start)
    for v in graph[start]:
        if v not in visit:
            dfs(v)
def bfs(start):
    global graph, visit
    queue = list()
    queue.append(start)
    visit.add(start)
    while queue:
        now = queue.pop()
        for v in graph[now]:
            if v not in visit:
                queue.append(v)
                visit.add(v)
# 그래프 초기화
for i in range(n):
    graph[i+1] = list()
# 간선 연결
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(1, n+1):
    if i not in visit:
        answer += 1
        bfs(i)
print(answer)