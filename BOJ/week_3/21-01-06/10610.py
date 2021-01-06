N = str(input())
stack = []
answer = 0
for i in N:
    stack.append(i)
stack.sort()
answer = int("".join(map(str, reversed(stack))))
if answer % 30 == 0:
    print(answer)
else:
    print(-1)