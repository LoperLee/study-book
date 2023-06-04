import sys

def resolve():
    pass

width, heigth = map(int, sys.stdin.readline().split(" "))
maps = []
for _ in range(heigth):
    maps.append(list(sys.stdin.readline()))