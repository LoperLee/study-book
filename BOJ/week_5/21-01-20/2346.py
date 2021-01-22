from collections import deque
N = int(input())
count, balloons = 1, deque()
for i in list(map(int, input().split())):
    balloons.append((count, i))
    count += 1
while balloons:
    value = balloons.popleft()
    if balloons:
        if value[1] > 0:
            for _ in range(value[1]-1):
                balloons.append(balloons.popleft())
        else:
            for _ in range((value[1]*-1)):
                balloons.appendleft(balloons.pop())
    print(value[0], end=" ")