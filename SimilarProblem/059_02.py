h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

mod = 10 ** 9 + 7
dp = [[0] * w for _ in range(h)]

def bfs(i: int, j: int) -> int:

    if dp[i][j] == 0:
        dp[i][j] = 1
 
        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):

            y = i + dy
            x = j + dx

            if not (0 <= y < h and 0 <= x < w):
                continue

            if a[y][x] < a[i][j]:
                dp[i][j] += bfs(y, x)
    
    return dp[i][j] % mod


for i in range(h):
    for j in range(w):
        bfs(i, j)

ans = 0
for i in range(h):
    for j in range(w):
        ans += dp[i][j]
        ans %= mod

print(ans)