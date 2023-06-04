import sys

answer = 0
people = 0
for _ in range(10):
    outp, inp = map(int, sys.stdin.readline().split())
    people += (inp - outp)
    if answer < people:
        answer = people
print(answer)