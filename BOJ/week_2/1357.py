X, Y = map(str, input().split())
ret = str(int(X[::-1]) + int(Y[::-1]))
print(int(ret[::-1]))