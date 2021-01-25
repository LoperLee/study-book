def paint_pixel(x, y):
    for py in range((y*K), (y*K)+K):
        for px in range((x*K), (x*K)+K):
            copy[py][px] = pixel[y][x]
N, K = map(int, input().split())
pixel, copy = [], [ [ 0 for _ in range(N*K)] for _ in range(N*K) ]
for _ in range(N):
    pixel.append(list(map(int, input().split())))
for y in range(N):
    for x in range(N):
        paint_pixel(x, y)
for c in copy:
    print(' '.join(map(str, c)))