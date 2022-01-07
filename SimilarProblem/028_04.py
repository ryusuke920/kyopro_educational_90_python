import sys
input = sys.stdin.readline

from collections import deque

def CC(A: list) -> list:
    B = {j: i for i, j in enumerate(sorted(set(A)))}
    return B

def main():
    w, h = map(int, input().split())
    n = int(input())
    w, h = min(w, 2 * n + 1), min(h, 2 * n + 1)

    xy = [list(map(int, input().split())) for _ in range(n)]
    x, y = [], []
    for i in range(n):
        x1, y1, x2, y2 = xy[i]
        x.append(x1)
        x.append(x2)
        y.append(y1)
        y.append(y2)

    cc_x = CC(x) # x座標を座圧 
    cc_y = CC(y) # y座標を座圧

    grid = [[0] * w for _ in range(h)]
    for i in range(n):
        x1, y1, x2, y2 = xy[i]
        for j in range(cc_y[y1], cc_y[y2] + 1):
            grid[j][cc_x[x1]] += 1
        for j in range(cc_y[y1], cc_y[y2] + 1):
            grid[j][cc_x[x2]] -= 1

    for i in range(h):
        for j in range(w - 1):
            grid[i][j + 1] += grid[i][j]

    d = ((0, 1), (0, -1), (1, 0), (-1, 0))
    ans = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0: continue
            ans += 1
            q = deque()
            q.append((i, j))
            while q:
                vy, vx = q.popleft()
                for dy, dx in d:
                    y = vy + dy
                    x = vx + dx
                    if not (0 <= x < w and 0 <= y < h): continue
                    if grid[y][x] != 0: continue
                    grid[y][x] = 1
                    q.append((y, x))

    print(ans)

if __name__ == '__main__':
    main()