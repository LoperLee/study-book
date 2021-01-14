from collections import deque
word, stan = deque(list(input())), input()
answer = 0
while word:
    now, count = word.popleft(), 0
    if now == stan[0] and len(word) >= len(stan)-1:
        count += 1
        for i in range(1, len(stan)):
            if word[i-1] == stan[i]:
                count += 1
            else:
                break
    else:
        continue
    if count >= len(stan):
        for _ in range(1, len(stan)):
            word.popleft() #중복제거
        answer += 1
print(answer)