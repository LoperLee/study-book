n = int(input())
a = 0
b = 1
while n > 1:
    tmp = b
    b = a + b
    a = tmp
    n -= 1
print(b)