n, m, k = map(int, input().split())
data = sorted(list(map(int, input().split())))
queue = [data[-1], data[-2]]
answer = 0
counter = 0
# for i in range(m):
#     if counter >= k:
#         answer += data[-2]
#         counter = 0
#         print(data[-2], end="+")
#         continue
#     answer += data[-1]
#     counter += 1
#     print(data[-1], end="+")

base = (m // k)
print(base)
answer += (data[-1] * (m - base))
answer += (data[-2] * base)

print(answer)