import sys

N = int(sys.stdin.readline())
results = []

for i in range(666, 1000 * N):
    numbering = str(i)
    if "666" in numbering:
        results.append(i)
    if len(results) >= N:
        break

print(results[N-1])