import sys
from collections import deque

N = int(sys.stdin.readline())
for _ in range(N):
    typing_left = deque()
    typing_right = deque()
    for value in list(sys.stdin.readline().replace("\n", "")):
        if value == "<":
            if typing_left:
                typing_right.appendleft(typing_left.pop())
        elif value == ">":
            if typing_right:
                typing_left.append(typing_right.popleft())
        elif value == "-":
            if typing_left:
                typing_left.pop()
        else:
            typing_left.append(value)
    print(''.join(typing_left + typing_right))
