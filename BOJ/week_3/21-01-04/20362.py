n, anick = map(str, input().split())
answer = 0
timeline = [] #stack0 = nick name, stack1 == chat
ansChat = ""
for _ in range(int(n)):
    nick, chat = map(str, input().split())
    if nick == anick:
        ansChat = chat
    if ansChat == "":
        timeline.append(chat)
for i in range(len(timeline)):
    if ansChat == timeline.pop():
        answer += 1
print(answer)