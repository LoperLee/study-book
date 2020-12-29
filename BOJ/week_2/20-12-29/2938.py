import sys
n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
anwser = True
for i in range(n):
    chk = False
    for j in range(i+1, n):
        print(array[i],array[j], (array[i]+array[j])%3)
        if (array[i]+array[j])%3 != 0:
            tmp = array[i+1]
            array[i+1] = array[j]
            array[j] = tmp
            chk = True
    if not chk:
        print(chk)
        break
if anwser:
    print(array)
else:
    print(-1)