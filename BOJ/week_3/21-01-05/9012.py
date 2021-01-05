N = int(input())
for _ in range(N):
    pstr = input()
    stack = []
    answer = "YES"
    for i in pstr:
        # print(answer, stack, i)
        if answer == "NO": break
        if i == "(":
            stack.append("(")
        elif i == ")":
            if len(stack) <= 0:
                answer = "NO"
            else:
                if stack.pop(0) != "(":
                    answer = "NO"
    if len(stack) > 0:
        answer = "NO"
    print(answer, stack)