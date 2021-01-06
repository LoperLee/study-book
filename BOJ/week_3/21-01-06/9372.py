import sys
N = int(sys.stdin.readline())
for _ in range(N):
    ver, edg = map(int, sys.stdin.readline().split())
    for _ in range(edg):
        x, y = map(int, sys.stdin.readline().split())
    print(ver-1)