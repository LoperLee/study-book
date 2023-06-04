import sys

words = [0] * 26
collect = ""
lines = sys.stdin.readlines()
for line in lines:
    collect += line.replace(" ", "")
for alpha in list(collect):
    position = ord(alpha) - 97
    if position < 0: continue
    words[position] += 1
print("".join([chr(i + 97) for i, v in enumerate(words) if max(words) == v]))