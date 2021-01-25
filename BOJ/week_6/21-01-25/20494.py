N = int(input())
customer, sushi, table = list(), dict(), list()
answer = 0
for _ in range(N):
    customer.append(input())
for cus in reversed(customer):
    for c in reversed(cus):
        if c not in sushi:
            sushi[c] = 0
            table.append(c)
        sushi[c] += 1
for su in table:
    answer += sushi[su]
print(answer)