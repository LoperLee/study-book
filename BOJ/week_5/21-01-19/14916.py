N = int(input())
answer = 0
if N in [1, 3]:
    print(-1)
elif (N % 5) % 2 == 0:
    answer, N = answer + (N // 5), (N % 5)
    answer, N = answer + (N // 2), (N % 2)
    print(answer)
else:
    answer = ((N // 5) - 1) + (((N % 5) + 5) // 2)
    print(answer)