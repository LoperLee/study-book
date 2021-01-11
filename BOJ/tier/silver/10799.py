import sys
pipe = sys.stdin.readline()
stack, prev, answer = [], "", 0
for i in pipe:
    if i == "(":
        stack.append("(")
    elif i == ")":
        stack.pop()
        if prev == "(":
            answer += len(stack)
        else:
            answer += 1
    prev = i
print(answer)