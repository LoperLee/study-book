n = list(map(int, input().split()))
anwser = ""
for i in range(1, len(n)):
    tmp = n[i-1] - n[i]
    if tmp == -1:
        anwser = "ascending"
    elif tmp == 1:
        anwser = "descending"
    else:
        anwser = "mixed"
        break
print(anwser)