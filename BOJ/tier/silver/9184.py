import sys
N = int(sys.stdin.readline())
answer = [0] * 1000001
answer[1], answer[2] = 1, 2
for n in range(3, N+1):
    answer[n] = (answer[n-1] + answer[n-2]) % 15746
print(answer[N])