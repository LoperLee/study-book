import sys
data = list()
for _ in range(int(sys.stdin.readline())):
    data.append(int(sys.stdin.readline()))
for i in sorted(data):
    print(i)