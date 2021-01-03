def gcd(a, b):
    left = b
    right = a % b
    while right != 0:
        left, right = right, left % right
    return left
a, b = map(int, input().split())
g = gcd(a, b)
print(g)
print((a*b)//g)