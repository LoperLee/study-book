import sys

N = int(sys.stdin.readline())
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
origin_maps = []
weakness_map = []
for _ in range(N):
    M = sys.stdin.readline().rstrip()
    origin_maps.append(list(M))
    weakness_map.append(list(M.replace('G', 'R')))

for x in range(N):
    for y in range(N):
        mx, my = (origin_maps[y][x + dx[x]]), (origin_maps[y + dy[y]][x])
        print((my, mx), status, field[my][mx])
        # 범위 초과시 넘김
        if mx < 0 or my < 0 or mx > N or mx > M:
            continue