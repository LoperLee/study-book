def factorial(num):
    if num <= 1:
        return num
    else:
        return num * factorial(num-1)
fac = int(input())
answer = factorial(fac)
print(answer <= 0 and 1 or answer)