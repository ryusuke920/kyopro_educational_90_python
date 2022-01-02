n = int(input())
dcs = [tuple(map(int, input().split())) for _ in range(n)]
dcs.sort(key = lambda x: x[0])

# dp[i][j] := i番目までの仕事でj日目までの仕事で得られる報酬の最大値
dp = [[0] * 5001 for _ in range(n + 1)]
for i in range(n):
    di, ci, si = dcs[i]
    for j in range(1, 5001):
        if j - ci >= 0 and j <= di:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - ci] + si, dp[i + 1][j - 1])
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i + 1][j - 1])

print(dp[-1][-1])