n, m = map(int,input().split())
a = [int(input()) for _ in range(m)]

mod = 10 ** 9 + 7
dp = [1] * (n + 1)
for i in range(m):
    dp[a[i]] = 0

for i in range(n - 1):
    if dp[i + 2] != 0:
        dp[i + 2] = dp[i + 1] + dp[i]

print(dp[n] % mod)