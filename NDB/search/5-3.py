def bfs(x, y):
    if (x, y) in visit:
        return 0
    queue.append([x, y])
    visit.add((x, y))
    while queue:
        scop = queue.pop(0)
        for mov in range(4):
            mx, my = scop[0] + moveX[mov], scop[1] + moveY[mov]
            if mx < 0 or my < 0 or mx >= M or my >= N:
                continue
            print((mx, my))
            if (mx, my) not in visit and field[my][mx] == 0:
                queue.append([mx, my])
                visit.add((mx, my))
    return 1
N, M = map(int, input().split())
answer = 0
moveX, moveY = [0, -1, 0, 1], [-1, 0, 1, 0] # u l d r
field = []
queue, visit = [], set()
for _ in range(N):
    field.append(list(map(int, input())))
for y in range(N):
    for x in range(M):
        if field[y][x] == 1:
            visit.add((x, y))
            continue
        answer += bfs(x, y)
print(answer)