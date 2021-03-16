# 연습문제 Level 2 - 최댓값과 최솟값
def solution(s):
    answer = sorted(list(map(int, s.split(' '))))
    return '{min} {max}'.format(min=answer[0], max=answer[-1])