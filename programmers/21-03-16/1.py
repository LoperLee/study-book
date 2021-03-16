# 정렬 Level 2 - H-Index
def solution(citations):
    answer, citations = 0, reversed(sorted(citations))
    for i, e in enumerate(citations):
        i += 1
        if i > e:
            break
        answer = i
    return answer

print(solution([3, 0, 6, 1, 5]))            # 3
print(solution([4, 4, 4, 5, 0, 1, 2, 3]))   # 4
print(solution([22, 42]))                   # 2
print(solution([0, 0 ,1 ,1]))               # 1