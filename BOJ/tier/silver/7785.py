import sys

N = int(sys.stdin.readline())
intra_net = dict()

for _ in range(N):
    name, status = map(str, sys.stdin.readline().replace("\n", "").split(" "))
    if name not in intra_net:
        intra_net[name] = 0
    intra_net[name] += 1 if status == "enter" else -1

answer = []
for key in intra_net.keys():
    if intra_net[key] > 0:
        answer.append(key)

for value in reversed(sorted(answer)):
    sys.stdout.write(f"{value}\n")