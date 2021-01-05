def find(n):
    if n == network[n]:
        return n
    else:
        re = find(network[n])
        network[n] = re
        return network[n]
def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        network[y] = x
        friend[x] += friend[y]
n = int(input())
network, friend = dict(), dict()
for _ in range(n):
    k = int(input())
    network, friend = dict(), dict()
    for _ in range(k):
        a, b = input().split()
        if a not in network:
            network[a] = a
            friend[a] = 1
        if b not in network:
            network[b] = b
            friend[b] = 1
        union(a, b)
        print(friend[find(a)])