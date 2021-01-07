N, M = map(int, input().split())
status = list(map(int, input().split()))
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1] # U:0(-1, 0) R:1(0, 1) D:2(1, 0) L:3(0, -1)
answer, point = 1, 0
field, visit = [], {(status[0], status[1])}
for _ in range(N):
    field.append(list(map(int, input().split())))
while point < 4:
    # 왼쪽 방향 바라보기
    status[2] -= 1
    if status[2] < 0:
        status[2] = 3
    # 이동칸 구하기
    mx, my = (status[0] + dx[status[2]]), (status[1] + dy[status[2]])
    print((my, mx), status, field[my][mx])
    # 범위 초과시 넘김
    if mx < 0 or my < 0 or mx > N or mx > M:
        continue
    if (mx, my) not in visit and field[my][mx] == 0:
        status[0], status[1] = mx, my
        visit.add((mx, my))
        answer += 1
        point = 0
    else:
        point += 1
print(answer)