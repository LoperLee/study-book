import sys

N = int(sys.stdin.readline())
next = int(N)
answer = 0
while True:
    answer += 1
    numbers = list(str(next))
    sum_all = sum(map(int, numbers))
    next = int(''.join([numbers[-1], list(str(sum_all))[-1]]))
    if next == N:
        break
print(answer)