from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
graph = dict()
top, answer = 0, list()
# 요소 생성
for i in range(1, N+1):
    graph[i] = list()
# 간선 연결
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[B].append(A)
# BFS
for i in range(1, N+1):
    task, visit, count = deque(), [False] * (N+1), 1
    task.append(i)
    visit[i] = True
    while task:
        for j in graph[task.popleft()]:
            if not visit[j]:
                visit[j] = True
                task.append(j)
                count += 1
    if top < count:
        answer = [i]
        top = count
    elif top == count:
        answer.append(i)
print(' '.join(map(str, sorted(answer))))