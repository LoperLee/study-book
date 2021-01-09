N = int(input())
words = dict()
for _ in range(N):
    word = input()
    if len(word) not in words:
        words[len(word)] = set()
    words[len(word)].add(word)
for key in sorted(words.keys()):
    for val in sorted(list(words[key])):
        print(val)