import sys
from collections import deque
N = int(sys.stdin.readline())
for i in range(N):
    # word = deque(list(sys.stdin.readline().strip()))
    word = sys.stdin.readline().strip()
    left, right = 0, (len(word) - 1) # 더블 포인터
    answer, bubun = 0, False
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            if bubun:
                break
            if word[left+1] == word[right] and not bubun:
                left += 2
                right -= 1
                answer, bubun = 1, True
            if word[left] == word[right-1] and not bubun:
                left += 1
                right -= 2
                answer, bubun = 1, True
            if not bubun:
                answer = 2
                break
    print(answer)