import sys
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
answer, winner = [0, 0], "D"
for i in range(10):
    if A[i] == B[i]:
        answer[0] += 1
        answer[1] += 1
    elif A[i] > B[i]:
        answer[0] += 3
        winner = "A"
    elif A[i] < B[i]:
        answer[1] += 3
        winner = "B"
print(' '.join(map(str, answer)))
if answer[0] == answer[1]: print(winner)
elif answer[0] > answer[1]: print("A")
elif answer[0] < answer[1]: print("B")