T = int(input())
match = {"b": "d", "d": "b", "p": "q", "q": "p"}
for test_case in range(1, T + 1):
    test = input()
    answer = []
    for i in reversed(range(len(test))):
        answer.append(match[test[i]])
    print('#{} '.format(test_case), end="")
    print(''.join(map(str, answer)))