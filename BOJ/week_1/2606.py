com = {}
visit = {}
ret = 0
for i in range(1, int(input())+1): # 컴퓨터 딕셔너리 초기화
    com[i] = list()
for _ in range(0, int(input())): # 간선 입력 받음
    t, f = map(int, input().split())
    com[t].append(f)
    com[f].append(t) # 이부분 헤맷음 (서로 간선 연결 시켜줘야 함)
def DFS(start):
    global com, visit, ret
    ret += 1
    visit[start] = True
    for ne in com[start]:
        if ne not in visit:
            DFS(ne)
DFS(1)
print(ret-1)