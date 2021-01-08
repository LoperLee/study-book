N = int(input())
array = dict()
for _ in range(N):
    X, Y = map(int, input().split())
    if Y not in array:
        array[Y] = list()
    array[Y].append(X)
for key in sorted(array.keys()):
    for val in sorted(array[key]):
        print(val, key)