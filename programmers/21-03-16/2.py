# 해시 Level 2 - 위장
def solution(clothes):
    answer, hmap = 1, dict()
    for clo in clothes:
        name, part = map(str, clo)
        if part not in hmap:
            hmap[part] = 0
        hmap[part] += 1
    for value in hmap.values():
        answer *= (value+1)
    return answer-1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))