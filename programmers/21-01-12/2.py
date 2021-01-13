# Level 3 가장 먼 노드
def solution(n, edge):
    answer = 0
    graph, visit, dist = dict(), set(), [0] * (n+1)
    for ver in range(1, n+1):
        graph[ver] = list()
    for ver in edge:
        graph[ver[0]].append(ver[1])
        graph[ver[1]].append(ver[0])
    # BFS 방식으로 탐색
    queue = [1]
    visit.add(1)
    while queue:
        block = queue.pop(0)
        for ver in graph[block]:
            if ver not in visit:
                dist[ver] = dist[block] + 1
                queue.append(ver)
                visit.add(ver)
    dist.sort()
    last = dist[-1]
    for i in reversed(dist):
        if last == i:
            answer += 1
        else:
            break
    return answer