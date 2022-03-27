n = int(input())
a = list(map(int, input().split()))

INF = 10 ** 18 
# dp[l][r] := l から r までの数列を取り除くまでに必要な最小コスト
dp = [[INF] * (2 * n + 1) for _ in range(2 * n + 1)]

# 初期化
for i in range(1, 2 * n + 1):
    dp[i][i] = 0

for l in range(2 * n + 1):
    for r in range(2 * n + 1):
        if l > r:
            dp[l][r] = 0

# 更新（全て 1-indexed）
for span in range(2, 2 * n + 1, 2):
    for l in range(1, 2 * n):
        r = l + span - 1
        if r > 2 * n: continue
        for mid in range(l, r, 2):
            dp[l][r] = min(dp[l][r], dp[l][mid - 1] + dp[mid][r])
        dp[l][r] = min(dp[l][r], dp[l + 1][r - 1] + abs(a[l - 1] - a[r - 1]))

print(dp[1][2 * n])