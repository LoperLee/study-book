import sys

N = int(sys.stdin.readline())
timelines = dict()
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split(" "))
    if start not in timelines:
        timelines[start] = set()
    timelines[start].add(end)

answer = 0
max_time = max(timelines.keys())
for i in sorted(timelines.keys()):
    job_queue = [ (x + 1, 1) for x in sorted(list(timelines[i])) ]
    while job_queue:
        job = job_queue.pop()
        if max_time < job[0]:
            if answer < job[1]:
                answer = job[1]
            continue
        if job[0] not in timelines:
            for idx in range(job[0] + 1, max_time):
                if idx not in timelines:
                    continue
                job_queue.append((idx, job[1]))
                break
            continue
        for x in sorted(list(timelines[job[0]])):
            job_queue.append((x + 1, job[1] + 1))
print(answer)