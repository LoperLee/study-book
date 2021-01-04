click = int(input())
A, B = 1, 0
for i in range(click):
    B, A = B + A, B
print(A, B)