n, l = map(int,input().split())
dp = [0] * (n + 1) # dp[i] := i段目に行くパターン数
dp[0] = 1
mod = 10 ** 9 + 7
for i in range(1, n + 1):
    if i < l:
        dp[i] = dp[i - 1]
    else:
        dp[i] = dp[i - 1] + dp[i - l] # １個前とl個前から飛んでくる
    dp[i] %= mod

print(dp[n])