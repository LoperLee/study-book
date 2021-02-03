N, K = map(int, input().split())
items = [[0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(1, N+1):
    W, V = map(int, input().split())
    for j in range(1, K+1):
        if j < W:
            items[i][j] = items[i-1][j]
        else:
            items[i][j] = max(items[i-1][j], items[i-1][j-W] + V)
print(items[N][K])