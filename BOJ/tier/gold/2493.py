import sys
N = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
stack, receive = [], [0] * N
for i in range(N):
    while stack:
        if stack[-1][1] > tower[i]:
            receive[i] = (stack[-1][0] + 1)
            break
        stack.pop()
    stack.append((i, tower[i]))
print(" ".join(map(str, receive)))