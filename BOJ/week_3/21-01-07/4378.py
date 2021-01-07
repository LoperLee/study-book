keyboard = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"
while True:
    try:
        word = input()
        answer = []
        for i in range(len(word)):
            finder = keyboard.find(word[i])
            if finder < 0 or word[i] in "`QAZ":
                answer.append(word[i])
                continue
            answer.append(keyboard[finder-1])
        print(''.join(answer))
    except:
        break