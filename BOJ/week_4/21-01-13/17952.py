import sys
N = int(sys.stdin.readline())
answer, task = 0, []
for _ in range(N):
    report = list(map(int, sys.stdin.readline().split()))
    if report[0] == 1:
        task.append([report[1], report[2]])
    if task:
        task[-1][1] -= 1
        if task[-1][1] == 0:
            answer += task.pop(-1)[0]
print(answer)