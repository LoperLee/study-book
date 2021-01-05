n, m = map(int, input().split())
queue, visit = [n], set()
answer = 0
while queue:
    point = False
    for _ in range(len(queue)):
        now = queue.pop(0)
        if now == m:
            point = True
            break
        if now > 0 and (now-1) not in visit:
            queue.append(now-1)
            visit.add(now-1)
        if now < 1000000 and (now+1) not in visit:
            queue.append(now+1)
            visit.add(now+1)
        if now*2 <= 1000000 and (now*2) not in visit:
            queue.append(now*2)
            visit.add(now*2)
    if point: break
    answer += 1
print(answer)