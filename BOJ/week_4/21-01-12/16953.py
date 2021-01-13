import sys
answer, point = 0, False
N, K = map(int, sys.stdin.readline().split())
queue, visit = [N], {N}
while queue:
    answer += 1
    for _ in range(len(queue)):
        base = queue.pop(0)
        multi, plus = (base * 2), int('{}{}'.format(base, 1))
        if base == K:
            point = True
            break
        if multi <= K and multi not in visit:
            queue.append(multi)
            visit.add(multi)
        if plus <= K and plus not in visit:
            queue.append(plus)
            visit.add(plus)
    if point:
        break
if point:
    print(answer)
else:
    print(-1)