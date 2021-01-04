tile = int(input())
a, b = 0, 1 # 피보나치수열의 시작
for i in range(tile-1):
    b, a = a + b, b
print(((a+b)*2) + (b*2))