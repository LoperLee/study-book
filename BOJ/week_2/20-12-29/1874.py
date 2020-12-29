origin = []
base = []
mirror = []
def mirroring():
    global origin, base, mirror
    cnt = 1
    for element in base:
        while cnt <= element:
            base.append(cnt)
            mirror.append("+")
            cnt += 1
        if base[-1] == element:
            print(base, base[0], base[-1])
            base.pop()
            mirror.append("-")
        else:
            mirror = ["NO"]
            break

for i in range(1, int(input())+1):
    origin.append(i)
    element = int(input())
    base.append(element)
mirroring()
for pp in mirror:
    print(pp)


# cnt = 1
# base = []
# mirror = []
# for i in range(int(input())):
#     element = int(input())
#     while cnt <= element:
#         base.append(cnt)
#         mirror.append("+")
#         cnt += 1
#     if base[-1] == element:
#         print(base, base[0], base[-1])
#         base.pop()
#         mirror.append("-")
#     else:
#         mirror = ["NO"]
# for pp in mirror:
#     print(pp)