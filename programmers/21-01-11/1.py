# Level2 스킬트리
def solution(skill, skill_trees):
    length = len(skill)
    answer = 0
    for tree in skill_trees:
        prev, count = -1, True
        for index in tree:
            finder = skill.find(index)
            if finder < 0:
                continue
            if (prev+1) == finder:
                prev = finder
            elif (prev+1) != finder:
                count = False
                break
        if count > 0:
            answer += 1
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))