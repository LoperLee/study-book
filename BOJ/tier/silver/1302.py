import sys
from collections import Counter
import heapq

N = int(sys.stdin.readline())
books = []
queue = []

for _ in range(N):
    books.append(sys.stdin.readline().replace("\n", ""))

# Counter로 같은 숫자 세기
count_books = Counter(books)

# 우선순위 큐로 정렬하기
for key in count_books.keys():
    heapq.heappush(queue, (count_books[key] * -1, key))

# 같은 값이 있으면 사전순으로 정렬해야 해서 우선 임시로 리스트에 담는다
same_sales = [ heapq.heappop(queue) ]
answer = [ same_sales[0][1] ]
while queue:
    value = heapq.heappop(queue)
    if value[0] != same_sales[0][0]:
        break
    same_sales.append(value)
    answer.append(value[1])
    answer.sort()

sys.stdout.write(answer[0])