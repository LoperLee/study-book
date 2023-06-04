N = int(input())
answer = 0
while 0 < N:
    if (N % 5) == 0:
        answer += N // 5
        N %= 5
    elif (N % 3) == 0:
        answer += N // 3
        N %= 3
    elif N > 5:
        answer += 1
        N -= 5
    else:
        answer += 1
        N -= 3
print(answer)