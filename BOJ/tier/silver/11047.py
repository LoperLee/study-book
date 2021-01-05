n, k = map(int, input().split())
coins = []
answer = 0
for _ in range(n):
    coins.append(int(input()))
for coin in reversed(coins):
    answer += k // coin
    k %= coin
print(answer)