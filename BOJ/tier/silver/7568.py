n = int(input())
people = []
answer = []
for i in range(n):
    kg, cm = map(int, input().split())
    answer.append(1)
    people.append([kg, cm])
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            answer[i] += 1
print(' '.join(map(str, answer)))