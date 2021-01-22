import sys
def get_flip():
    ret, last = 1, 0
    for i in range(len(paint)-1):
        if (paint[i] + 1) != paint[i+1]:
            ret += 1
    return ret
N, M = map(int, sys.stdin.readline().split())
road = list(map(int, sys.stdin.readline().split()))
paint, answer = list(), 0
for _ in range(M):
    value = list(map(int, sys.stdin.readline().split()))
    if value[0] == 0:
        print(answer)
    else:
        if road[value[1]-1] == 0:
            road[value[1]-1] = 1
            paint.append(value[1])
            paint.sort()
        answer = get_flip()