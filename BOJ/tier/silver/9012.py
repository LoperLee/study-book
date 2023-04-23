import sys
from collections import deque

N = int(sys.stdin.readline())

for _ in range(N):
    left = deque()
    answer = "YES"
    for value in list(sys.stdin.readline().replace("\n", "")):
        if value == "(":
            left.append("(")
            continue
        if not left:
            answer = "NO"
            break
        left.pop()
    if answer == "YES" and left:
        answer = "NO"
    sys.stdout.write(answer + "\n")
