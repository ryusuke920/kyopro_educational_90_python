h, w = map(int,input().split())
s = [list(input()) for _ in range(h)]

dist = [[-1] * w for _ in range(h)]
d = ((1, 0), (-1, 0), (0, 1), (0, -1))

def dfs(y: int, x: int, cnt) -> int:
    if dist[y][x] != -1:
        if cnt - dist[y][x] >= 4:
            return cnt - dist[y][x]
        else:
            return -1

    num = -1
    dist[y][x] = cnt
    for dy, dx in d:
        if not (0 <= dy + y <= h - 1 and 0 <= dx + x <= w - 1): continue
        if s[dy + y][dx + x] == "#": continue
        num = max(num, dfs(dy + y, dx + x, cnt + 1))    
    dist[y][x] = -1

    return num

ans = -1
for i in range(h):
    for j in range(w):
        if s[i][j] == "#": continue
        ans = max(ans, dfs(i, j, 0))

print(ans)