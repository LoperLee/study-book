n = int(input())
shopping = list(map(int, input().split()))
ret = 0
for i in range(n):
    cost = 3
    j = 1
    if shopping[i] == 0:
        continue
    else:
        shopping[i] -= 1
    while j < 3 and i+j < n:
        if shopping[i+j] == 0:
            break
        else:
            shopping[i+j] -= 1
            cost += 2
        j += 1
    print(cost)
    ret += cost
print(ret)