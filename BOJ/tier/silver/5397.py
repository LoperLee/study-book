n = int(input())
for _ in range(n):
    keylog = str(input())
    left = []
    right = []
    for wd in keylog:
        if wd == "<":
            if left:
                right.append(left.pop())
        elif wd == ">":
            if right:
                left.append(right.pop())
        elif wd == "-":
            if left:
                left.pop()
        else:
            left.append(wd)
    print(''.join(left + right[::-1]))