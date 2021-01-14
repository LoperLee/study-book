from collections import deque
T = int(input())
left, right = [0, 0], [0, 0]
trophy = []
for _ in range(T):
    trophy.append(int(input()))
for i in range(len(trophy)):
    if left[0] < trophy[i]:
        left[0] = trophy[i]
        left[1] += 1
    if right[0] < trophy[len(trophy)-1-i]:
        right[0] = trophy[len(trophy)-1-i]
        right[1] += 1
print(left[1])
print(right[1])