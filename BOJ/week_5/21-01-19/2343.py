N, M = map(int, input().split())
lesson = list(map(int, input().split()))
answer = 0
left, right = 0, N-1
for x in range(M):
    mid = (left + right) // 2
    if x == M-1:
        mid = right
    count = 0
    for i in lesson[left:mid+1]:
        count += i
    if answer < count:
        answer = count
    left = mid+1
print(answer)