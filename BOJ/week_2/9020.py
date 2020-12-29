def isDec(value):
    ret = list()
    for i in range(2, value):
        chk = True
        for j in range(2, i):
            if i%j == 0:
                chk = False
                break
        if chk:
            ret.append(i)
    return ret

sosu = isDec(10000)
for x in range(0, int(input())):
    now = 0
    value = int(input())
    for i in sosu:
        if value-i in sosu and i <= value-i:
            now = i
    print(value, now, value-now)