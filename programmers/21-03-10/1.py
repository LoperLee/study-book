# Level 2 - 더 맵게
import heapq
def solution(scoville, K):
    answer, reach = 0, False
    heapq.heapify(scoville)
    while len(scoville) > 1:
        left, right = heapq.heappop(scoville), heapq.heappop(scoville)
        if left >= K:
            reach = True
            break
        heapq.heappush(scoville, (left + (right * 2)))
        answer = answer + 1
    if reach or heapq.heappop(scoville) >= K:
        return answer
    return -1

print(solution([1, 2, 3, 9, 10, 12]	, 7))