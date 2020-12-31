n = int(input())
idx = 0
answer = 0
while idx < n:
    value = n-idx
    compare = 0
    for i in str(value):
        compare += int(i)
    if n == (value + compare): # 비교값이 동일한가?
        if answer <= 0 or int(value) < answer: # 정답이 초기값이거나 정답보다 작은가?
            answer = int(value) # 기준값으로 변경하라
    idx += 1
print(answer)