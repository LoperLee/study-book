T = int(input())
books, best = dict(), ("", 0)
for _ in range(T):
    book = input()
    if book not in books:
        books[book] = 0
    books[book] += 1
    if best[1] < books[book]:
        best = (book, books[book])
    elif best[1] == books[book]:
        book = sorted([best[0], book])[0]
        best = (book, books[book])
print(best[0])