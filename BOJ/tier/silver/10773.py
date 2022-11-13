from functools import reduce
import sys

K = int(sys.stdin.readline())
stack = []

for _ in range(K):
    N = int(sys.stdin.readline())
    if N == 0 and len(stack) > 0: stack.pop()
    else: stack.append(N)

print(reduce(lambda acc, cur: acc + cur, stack, 0))