import sys

N = int(sys.stdin.readline())
array_a = sorted(list(map(int, sys.stdin.readline().split(" "))), reverse=True)
array_b = sorted(list(map(int, sys.stdin.readline().split(" "))))
answer = 0
for i in range(N):
    answer += (array_a[i] * array_b[i])
print(answer)