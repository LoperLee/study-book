n = int(input())
cpu = list(map(int, input().split()))
prev = 0
ret = 0
for i in range(n-1):
    prev = int(((prev*cpu[i])+cpu[i])%(1e9+7))
    ret += int(prev%(1e9+7))
print(ret)