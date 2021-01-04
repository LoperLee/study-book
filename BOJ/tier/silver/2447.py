def star(n, x, y):
    global paint
    base = n//3
    if n <= 3:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                paint[y+i][x+j] = 1
    else:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                star(base, x+(base*i), y+(base*j))
n = int(input())
paint = [[0 for _ in range(n)] for _ in range(n)]
star(n, 0, 0)
for y in paint:
    for x in y:
        if x == 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()