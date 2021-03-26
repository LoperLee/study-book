from functools import reduce
def get_one_count(binary):
    return reduce(lambda acc, cur: acc + cur, list(map(int, binary[2:])), 0)

def solution(n):
    answer, origin = n, get_one_count(bin(n))
    while (True):
        answer += 1
        if origin == get_one_count(bin(answer)):
            break
    return answer

print(solution(78)) # 83
print(solution(15)) # 23