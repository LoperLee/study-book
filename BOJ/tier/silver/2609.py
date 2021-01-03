def gcd(a, b):
    left = b
    right = a % b
    while right != 0:
        left, right = right, left % right
    return left
for _ in range(int(input())):
    a, b = map(int, input().split())
    print((a*b)//gcd(a, b))