def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        now, pre = 0, 1 if len(skill) <= 1 else len(skill)-1
        for seq in tree:
            if now == pre:
                break
            finder = skill.find(seq)
            if finder < 0:
                continue
            elif finder > now:
                break
            elif finder == now:
                now += 1
        print(now)
        if now == pre:
            answer += 1
    return answer
a = solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])
print("ans", a)