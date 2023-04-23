import sys

N, K = map(int, sys.stdin.readline().split(" "))
index = 0
origin = [ i for i in range(1, N + 1) ]
yose = []

while len(yose) < N:
    index += (K - 1)
    while len(origin) <= index: index -= len(origin)
    yose.append(origin.pop(index))

sys.stdout.write("<")
sys.stdout.write(", ".join(map(str, yose)))
sys.stdout.write(">")

# 1 2 3 4 5 6 7
# 0 1 2 3 4 5 6