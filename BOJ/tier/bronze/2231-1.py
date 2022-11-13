import sys
from functools import reduce

N = int(sys.stdin.readline())
results = []

for i in reversed(range(1, N)):
    sum_all = reduce(lambda acc, cur: acc + int(cur), list(str(i)), i)
    if sum_all == N:
        results.append(i)
        
if len(results) <= 0:
    print(0)
else:
    print(min(results))