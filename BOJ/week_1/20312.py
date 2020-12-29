n = int(input())
array = list(map(int, input().split()))
last, length = 0
ret = 0
for i in range(n-1):
    prev.append(array[i])
    prev[0] = int(prev[0]*array[i])
    print("===", prev[0] * len(prev), prev[0], len(prev), "===")
    ret += (prev[0] * len(prev))
    ret += array[i]
    print(prev, ret)
print(ret%((10**9)+7))