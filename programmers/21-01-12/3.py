# Level 3 
def solution(a):
    answer, pointer = set(), 0
    while pointer < len(a)-1:
        delete = []
        lower, npoint = False, pointer + 1
        for _ in range(len(a)-1):
            print(pointer)
            if a[pointer] < a[npoint]:
                delete.append(a[npoint])
            elif not lower:
                delete.append(a[npoint])
                lower = True
            if npoint < len(a)-1:
                npoint += 1
            else:
                if pointer >= (len(a) - len(delete)):
                    pointer -= 1
                npoint -= 1
        print(delete, npoint)
        if (len(a) - 1) == len(delete):
            answer.add(a[pointer])
        pointer += 1
    return len(answer)
print(solution([9,-1,-5]))