n = int(input())
graph = {}
visit = {}
for _ in range(n):
    t, i, f = map(str, input().split())
    if t not in graph:
        graph[t] = list()
        visit[t] = False
    if f not in graph:
        graph[f] = list()
        visit[f] = False
    graph[t].append(f)

if "Baba" in graph:
    queue = []
    queue.append("Baba")
    visit["Baba"] = True
    while len(queue) > 0:
        now = queue.pop()
        for value in graph[now]:
            if not visit[value]:
                visit[value] = True
                queue.append(value)
    visit["Baba"] = False
    for value in sorted(list(visit.keys())):
        if visit[value]:
            print(value)