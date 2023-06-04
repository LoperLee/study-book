import sys

def dfs(position):
    global a_list, visit
    if position in visit or (len(a_list) <= position or position < 0):
        return
    visit.add(position)
    jump = a_list[position]
    dfs(position - jump)
    dfs(position + jump)

visit = set()
n = int(sys.stdin.readline())
a_list = list(map(int, sys.stdin.readline().split()))
s = int(sys.stdin.readline())

dfs(s - 1)
print(len(visit))