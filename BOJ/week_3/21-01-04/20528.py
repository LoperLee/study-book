n = int(input())
data = input().split()
point = data[0][0]
answer = 1
for i in data:
    if i[0] != point:
        answer = 0
        break
print(answer)