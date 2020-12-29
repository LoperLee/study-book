import sys
stack = []
for _ in range(int(sys.stdin.readline())):
    order = sys.stdin.readline().split()
    if order[0] == "push": stack.append(order[1])
    elif order[0] == "pop": print(stack and stack.pop(0) or -1)
    elif order[0] == "size": print(len(stack))
    elif order[0] == "empty": print(not stack and 1 or 0)
    elif order[0] == "front": print(len(stack) <= 0 and -1 or stack[0])
    elif order[0] == "back": print(len(stack) <= 0 and -1 or stack[len(stack)-1])