from collections import deque
def getPrime(num):
    ret = [2, 3]
    for i in range(5, num):
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
T = int(input())
prime = getPrime(1001)
for _ in range(T):
    start, end = map(int, input().split())
    task, visit = deque([start]), {start}
    while task:
        for _ in range(len(task)):
            now = task.popleft()
            if now not in prime:
                continue
            for i in range(1, 10):
                for jari in [1, 10, 100, 1000]:
                    tmp = now + (jari * i)
                    if tmp in prime:
                        
                if (now + i) not in visit:
                    visit
