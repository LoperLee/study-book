origin_count = 0
dp_count = 0

def fibo_origin(n):
    global origin_count
    if (n == 1 or n == 2):
        origin_count += 1
        return 1
    else:
        return fibo_origin(n-1) + fibo_origin(n-2)

def fibo_dp(n):
    global dp_count
    table = [0, 1, 1] + [0] * n
    for i in range(3, n + 1):
        dp_count += 1
        table[i] = table[i - 1] + table[i - 2]

N = int(input())
fibo_origin(N)
fibo_dp(N)
print(origin_count, dp_count)