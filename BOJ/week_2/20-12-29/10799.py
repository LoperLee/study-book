pipe = input()
stack = []
anwser = 0
for line in pipe:
    if line == "(":
        stack.append("(")