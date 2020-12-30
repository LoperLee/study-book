n, m = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()
anwser = 0
for i in range(n-1, 1, -1):
    for j in range(i-1, 0, -1):
        if m <= (cards[i]+cards[j]):
            break
        for x in range(j-1, -1, -1):
            value = (cards[i]+cards[j]+cards[x])
            if anwser < value and value <= m:
                anwser = value
    if anwser == m:
        break
print(anwser)