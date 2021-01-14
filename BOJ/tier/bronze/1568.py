K = int(input())
answer, song = 0, 1
while K > 0:
    K -= song
    song += 1
    if K < song:
        song = 1
    answer += 1
print(answer)