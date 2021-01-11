# Level2 삼각 달팽이
def solution(n):
    brute = []
    weight, count, answer = 0, 1, []
    for i in range(1, n+1):
        brute.append([0] * i)
    # 일단 무작정 다 넣어보자
    while weight <= n//2:
        length = n - weight
        for i in range(weight, length):
            if brute[i][weight] != 0:
                continue
            brute[i][weight] = count
            count += 1
        print(brute)
        for i in range(1, length):
            if brute[length-1][i] != 0:
                continue
            brute[length-1][i] = count
            count += 1
        print(brute)
        for i in reversed(range(weight, length)):
            print((i, i-weight), brute[i][i-weight], weight)
            if brute[i][i-weight] != 0:
                continue
            brute[i][i-weight] = count
            count += 1
        print(brute)
        weight += 1
    for x in brute:
        for y in x:
            answer.append(y)
    return answer

print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))
print(solution(8))
print(solution(9))