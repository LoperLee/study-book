import sys
from collections import Counter

words = sys.stdin.readline().rstrip('\n')
words = words.upper()

result = list(Counter(list(words)).items())
result.sort(key=lambda tup: tup[1])
if len(result) == 1 or result[-1][1] != result[-2][1]:
    print(result[-1][0])
else:
    print("?")