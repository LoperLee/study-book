import copy
import sys

N, M = map(int, sys.stdin.readline().split(" "))
board = []
for _ in range(N):
    board.append(list(sys.stdin.readline()))

# 각 4개의 변에서 시작해서 가장 적게 칠하는 값을 구한다.
answer = 99999999
paint = {"B": "W", "W": "B"}
points = [
    {'start': (range(N), range(M)), 'check': [(0, 1), (1, 0)]},
    {'start': (range(N), reversed(range(M))), 'check': [(0, -1), (1, 0)]},
    {'start': (reversed(range(N)), range(M)), 'check': [(0, 1), (-1, 0)]},
    {'start': (reversed(range(N)), reversed(range(M))), 'check': [(0, -1), (-1, 0)]}
]
for data in points:
    board_copy = copy.deepcopy(board)
    sum_all = 0
    for y in data['start'][0]:
        for x in data['start'][1]:
            for cY, cX in data['check']:
                next_x = (x + cX)
                next_y = (y + cY)
                if (N <= next_y or next_y < 0):
                    continue
                if (M <= next_x or next_x < 0):
                    continue
                point1 = board_copy[y][x]
                point2 = board_copy[next_y][next_x]
                if board_copy[y][x] == board_copy[next_y][next_x]:
                    board_copy[next_y][next_x] = paint[board_copy[next_y][next_x]]
                    sum_all += 1
    if sum_all < answer:
        answer = sum_all
print(answer)