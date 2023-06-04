import sys

def find(x):
    if groups[x] == x:
        return x
    re = find(groups[x])
    groups[x] = re
    return groups[x]
def union(x, y):
    left = find(x)
    right = find(y)
    if left != right:
        if costs[left-1] < costs[right-1]:
            groups[right] = left
        else:
            groups[left] = right

N, M, money = map(int, sys.stdin.readline().split())
costs = list(map(int, sys.stdin.readline().split()))
groups = [ idx for idx in range(N+1) ]
visite = [ False for _ in range(N+1) ]
for _ in range(M):
    v, w = map(int, sys.stdin.readline().split())
    union(v, w)
    
answer = 0
for i in range(1, N+1):
    person = find(i)
    if not visite[person]:
        answer += costs[person-1]
        visite[person] = True

print(answer if answer <= money else "Oh no")