n, k = map(int,input().split())
a, b = [0] * n, [0] * n
for i in range(n):
    a[i], b[i] = map(int,input().split())

h, w = max(a) + 1, max(b) + 1
grid = [[0] * w for _ in range(h)]
for i in range(n):
    grid[a[i]][b[i]] += 1

for i in range(1, h - 1):
    for j in range(1, w):
        grid[i + 1][j] += grid[i][j]

for i in range(1, h):
    for j in range(1, w - 1):
        grid[i][j + 1] += grid[i][j]

# grid[i][j] := グループ内の身長の最小値がiで体重の最小値がjである場合
# これを満たす最大の範囲は身長が i以上i+k 以下、体重が j以上j+k以下 である。
ans = 0
for i in range(1, h):
    for j in range(1, w):
        ii = min(h - 1, i + k)
        jj = min(w - 1, j + k)
        people = grid[ii][jj] - grid[ii][j - 1] - grid[i - 1][jj] + grid[i - 1][j - 1]
        ans = max(ans, people)

print(ans)