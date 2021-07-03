n = int(input())
a = list(map(int,input().split()))
ans = a.pop()

# dp[i][j] := i番目までの数字でj以下の数を超えない場合の数(j <= 20)
dp = [[0] * 21 for _ in range(n - 1)]
dp[0][a[0]] = 1
for i in range(n - 2):
    for j in range(21):
        if 0 <= j + a[i + 1] <= 20:
            dp[i + 1][j + a[i + 1]] += dp[i][j]
        if 0 <= j - a[i + 1] <= 20:
            dp[i + 1][j - a[i + 1]] += dp[i][j]

print(dp[-1][ans])