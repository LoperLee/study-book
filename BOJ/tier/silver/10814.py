n = int(input())
data = dict()
for _ in range(n):
    age, name = map(str, input().split())
    if int(age) not in data:
        data[int(age)] = list()
    data[int(age)].append(name)
for key in sorted(list(data.keys())):
    for name in data[key]:
        print(key, name)