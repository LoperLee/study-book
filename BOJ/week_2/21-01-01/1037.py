n = int(input())
m = sorted(list(map(int, input().split())))
answer = m[0] * m[-1]
print(answer)