import sys
N, M = map(int, sys.stdin.readline().split(" "))
result = 0
hashmap = set()
for _ in range(N):
    hashmap.add(sys.stdin.readline())
for _ in range(M):
    word = sys.stdin.readline()
    if word in hashmap:
        result += 1
print(result)