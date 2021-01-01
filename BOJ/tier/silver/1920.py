n = int(input())
nA = set(map(int, input().split()))
m = int(input())
mA = list(map(int, input().split()))
for col in mA:
    if col in nA:
        print(1)
    else:
        print(0)