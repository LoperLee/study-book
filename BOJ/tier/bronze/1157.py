word = input()
top, answer = 0, []
alpa = {}
for i in word.lower():
    if i not in alpa:
        alpa[i] = 0
    alpa[i] += 1
for key, val in alpa.items():
    if top < val:
        top = val
        answer = [key]
    elif top == val:
        answer.append(key)
print("?" if len(answer) > 1 else answer[0].upper())