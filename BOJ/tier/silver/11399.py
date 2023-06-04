import sys

N = int(sys.stdin.readline())
times = sorted(list(map(int, sys.stdin.readline().split())))
answer = 0
for i in range(N):
    answer += sum(times[:i+1])
print(answer)