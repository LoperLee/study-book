n = input()
data = list()
for i in n:
    data.append(i)
print(''.join(reversed(sorted(data))))