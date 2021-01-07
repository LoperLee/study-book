import sys
def fibo(n):
    if len(answer[n]) > 0:
        return answer[n]
    x, y = fibo(n-1), fibo(n-2)
    answer[n] = [x[0]+y[0], x[1]+y[1]]
T = int(sys.stdin.readline())
answer = [[]] * 41
answer[0], answer[1] = [1, 0], [0, 1]
for i in range(2, 41):
    fibo(i)
for _ in range(T):
    N = int(sys.stdin.readline())
    if N == 0:
        print(1, 0)
    elif N == 1:
        print(0, 1)
    else:
        print(' '.join(map(str, answer[N])))