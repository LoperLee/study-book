def fibo(num):
    if num < 2:
        if num == 1:
            return 1
        if num == 0:
            return 0
    else:
        return (fibo(num-1)+fibo(num-2))
fi = int(input())
print(fibo(fi))