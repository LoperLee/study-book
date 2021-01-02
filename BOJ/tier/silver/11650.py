n = int(input())
data = dict()
for _ in range(n):
    x, y = map(int, input().split())
    if x not in data:
        data[x] = list()
    data[x].append(y)
for x in sorted(list(data.keys())):
    for y in sorted(data[x]):
        print(x, y)