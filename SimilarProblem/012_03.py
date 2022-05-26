from collections import deque

def bfs(sx: int, sy: int) -> bool:
    dist = [[INF] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "#":
                dist[i][j] = -1
    dist[sx][sy] = 0
    q = deque()
    q.append((sx, sy))
    while q:
        vy, vx = q.popleft()
        for dy, dx in d:
            if not (0 <= vy + dy <= h - 1 and 0 <= vx + dx <= w - 1): continue
            if dist[vy + dy][vx + dx] != INF: continue
            if grid[vy + dy][vx + dx] == "#": continue
            dist[vy + dy][vx + dx] = dist[vy][vx] + 1
            q.append((vy + dy, vx + dx))

    for i in range(h):
        for j in range(w):
            if dist[i][j] == INF:
                return False
    
    return True

h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
INF = 10 ** 18

ans = 0
for i in range(h):
    for j in range(w):
        if grid[i][j] == "#":
            if bfs(i, j):
                ans += 1

print(ans)