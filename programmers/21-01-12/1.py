# Level2 가장 큰 수
def solution(numbers):
    nums = [[] for _ in range(5)] # 최대 1000까지
    answer = []
    for i in numbers:
        nums[len(str(i))].append(i)
    print(nums)
    for i in range(1, 5):
        for j in reversed(sorted(nums[i])):
            answer.append(j)
    return ''.join(map(str, answer))

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))