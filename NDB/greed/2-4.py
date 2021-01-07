N, K = map(int, input().split())
answer = 0
while N > 1:
    N -= 1
    N //= 3
    answer += 1
print(answer)