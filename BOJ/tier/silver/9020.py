import sys
def sosuList(value):
    ret = [2, 3]
    for i in range(5, value):
        chk = True
        for j in ret:
            if i < (j*j):
                break
            if i%j == 0:
                chk = False
                break
        if chk:
            ret.append(i)
    return ret
sosu = sosuList(10000) # 에라토스테네스의 체를 이용해 미리 소수 리스트를 만들어둠
for _ in range(int(sys.stdin.readline())):
    now = 0
    value = int(sys.stdin.readline())
    half = int(value/2) # 입력은 짝수만이 들어옴 때문에 소수점 고려X
    while True:
        if (half-now) in sosu and (half+now) in sosu:
            break
        now += 1
    print(half-now, half+now)