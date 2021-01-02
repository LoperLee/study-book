import sys
def find(col):
    if col == parent[col]:
        return col
    else:
        re = find(parent[col])
        parent[col] = re
        return parent[col]
def union(x, y):
    x = find(x)
    y = find(y)
    parent[y] = x
n, m = map(int, sys.stdin.readline().split())
parent = list()
for i in range(n+1):
    parent.append(i)
for _ in range(m):
    c, a, b = map(int, sys.stdin.readline().split())
    if c == 0:
        union(a, b)
    if c == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")