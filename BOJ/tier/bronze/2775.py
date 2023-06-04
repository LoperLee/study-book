import sys

T = int(sys.stdin.readline())
for _ in range(T):
    K = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    table = [ i for i in range(N+1) ]
    for _ in range(K):
        for i in range(1, N+1): 
            table[i] = table[i] + table[i-1]
    print(table[-1])