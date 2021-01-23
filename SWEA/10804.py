T = int(input())
match = {"b": "d", "d": "b", "p": "q", "q": "p"}
for test_case in range(1, T + 1):
    test = input()
    for i in test:
        test = test.replace(i, match[i])
    print(test[::-1])