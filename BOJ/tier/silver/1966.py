for _ in range(int(input())):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    answer = 0
    while True:
        doc = queue.pop(0)
        upper = False
        for other in queue:
            if doc < other:
                upper = True
                break
        if upper:
            queue.append(doc)
            if m <= 0:
                m = len(queue)
        else:
            answer += 1
            if m == 0:
                break
        m -= 1
    print(answer)