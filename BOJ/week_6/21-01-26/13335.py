from collections import deque
N, W, L = map(int, input().split())
trucks = list(map(int, input().split()))
answer, bridge, now_weight = 1, deque(), 0
while True:
    answer += 1
    if trucks and (now_weight + trucks[0]) <= L:
        inner = trucks.pop(0)
        now_weight += inner
        bridge.append([inner, 0])
    for i in range(len(bridge)):
        bridge[i][1] += 1
    if bridge[0][1] >= W:
        now_weight -= bridge.popleft()[0]
    if not bridge and not trucks:
        break
print(answer)