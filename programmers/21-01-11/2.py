# Level2 문자열 압축
def solution(s):
    answer = len(s)
    for i in range(1, len(s)+1):
        count, press, word = 0, [], []
        # 문자열을 잘라냄
        for count in range(i, len(s)+1, i):
            press.append(s[count-i:count])
        if count < len(s): # 남은 문자열 있으면 넣어줌
            press.append(s[count:len(s)])
        press.append("")
        # 잘라낸 문자열 비교
        count, prev = 1, press.pop(0)
        while press:
            key = press.pop(0)
            # print(key, count, prev)
            if prev == key:
                count += 1
                continue
            if count <= 1:
                word.append('{}'.format(prev))
            else:
                word.append('{}{}'.format(count, prev))
            count = 1
            prev = key
        prev = ''.join(map(str, word))
        # 압축된 문자열 카운팅
        if len(prev) < answer:
            answer = len(prev)
    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))