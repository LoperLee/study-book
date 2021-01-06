def solution(board, moves):
    answer = 0
    stack = []
    for x in moves:
        for y in range(len(board)):
            toy = board[y][x-1]
            if toy > 0:
                board[y][x-1] = 0
                if stack:
                    if stack[-1] == toy:
                        answer += 2
                        stack.pop(-1)
                        break
                stack.append(toy)
                break
    return answer
a = solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
print(a)