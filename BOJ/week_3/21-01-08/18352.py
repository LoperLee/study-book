import sys
N, M, K, X = map(int, sys.stdin.readline().split())
answer, graph, visit = list(), dict(), set()
dist = [0] * (N+1)
for i in range(1, N+1):
    graph[i] = list()
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
# BFS
queue = [(X, 0)]
visit.add(X)
while queue:
    vert, count = queue.pop(0)
    if count == K:
        answer.append(vert)
    elif count < K:
        for i in graph[vert]:
            if i not in visit:
                queue.append((i, count+1))
                visit.add(i)
if len(answer) <= 0:
    print(-1)
else:
    print('\n'.join(map(str, sorted(answer))))