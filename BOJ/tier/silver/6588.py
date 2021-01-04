import sys
def getPrime(n):
    sosu = {i for i in range(2, n)}
    for i in range(2, n):
        if i in sosu:
            for j in range(i+i, n, i):
                if j in sosu: sosu.remove(j)
    return sosu
sosu = getPrime(1000000)
while True:
    tcase = int(sys.stdin.readline())
    answer = False
    if tcase == 0:
        break
    for i in range(3, (tcase//2)+1):
        if i not in sosu:
            continue
        if (i % 2) == 0:
            continue
        if (tcase - i) in sosu:
            answer = True
            print('%d = %d + %d' % (tcase, i, (tcase - i)))
            break
    if not answer:
        print("Goldbach's conjecture is wrong.")