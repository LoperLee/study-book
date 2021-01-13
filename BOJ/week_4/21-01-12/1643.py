while True:
    N = input()
    if N == "*":
        break
    answer = True
    if len(N) > 1:
        if not answer:
            break
        for i in range(1, len(N)):
            words, visit, select = list(N), set(), set()
            for j in range(len(words)):
                if j in select:
                    continue
                if j+i >= len(words):
                    break
                word = '{}{}'.format(words[j], words[j+i])
                if word in visit:
                    answer = False
                    break
                visit.add(word)
    if answer:
        print('{} is surprising.'.format(N))
    else:
        print('{} is NOT surprising.'.format(N))