n, m = map(int, input().split())
days = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4}
for i in range(m):
    d1, d2, d3, d4 = map(str, input().split())
    n -= (((24*(days[d3]-days[d1]))+int(d4))-int(d2))
if n <= 0:
    print(0)
elif n > 48:
    print(-1)
else:
    print(n)