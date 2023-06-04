import sys

def resolve(buildings) :
    # 해답부
    prev = buildings.pop()
    hight = prev
    count = 0
    answer = 0
    while buildings:
        now = buildings.pop()
        count += 1
        if prev < now:
            if hight < now:
                hight = now
                answer += answer
            answer += count
            count = 0
        prev = now
    return answer

# 입력부
answer = 0
buildings = []
N = int(sys.stdin.readline())
for _ in range(N):
    buildings.append(int(sys.stdin.readline()))

print(resolve(buildings))