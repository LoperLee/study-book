croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
strings = input()
for idx in croatia:
    while strings.find(idx) > -1:
        strings = strings.replace(idx, " ", 1)
print(len(strings))