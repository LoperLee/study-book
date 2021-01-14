n, m = map(int, input().split()) # 세로, 가로
height, width = [False] * n, [False] * m
for i in range(n):
    guarder = input()
    for bat in range(len(guarder)):
        if guarder[bat] == "X":
            width[bat] = True
            height[i] = True
row = [0, 0]
for i in range(n):
    if not height[i]:
        row[0] += 1
for i in range(m):
    if not width[i]:
        row[1] += 1
print(max(row))