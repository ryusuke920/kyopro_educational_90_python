n, m = map(int, input().split())

dp = [0] * (n + 1)
dp[2] = 1

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
    dp[i] %= m

print(dp[n])