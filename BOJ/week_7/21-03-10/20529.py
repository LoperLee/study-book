T = int(input())
for _ in range(T):
    answer = 10e6
    N = int(input())
    people = list(map(str, input().split()))
    # 중복 제거
    if N > 32:
        print(0)
    else:
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp = 0
                    if i == j or j == k or i == k:
                        continue
                    for x in range(4):
                        if people[i][x] != people[j][x]: tmp += 1
                        if people[j][x] != people[k][x]: tmp += 1
                        if people[i][x] != people[k][x]: tmp += 1
                    answer = min(tmp, answer)
        print(answer)