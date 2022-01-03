n, p = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]
ab.sort(key=lambda x: -x[0])

dp = [0] * 5101
ans = 0
for i in range(n):
    a, b = ab[i]
    for j in reversed(range(p + 101)):
        if j - a >= 0:
            dp[j] = max(dp[j], dp[j - a] + b)
        # 金額j - i番目のおやつaを引いてもp以下なら遷移可能
        if j - a <= p:
            ans = max(ans, dp[j])

print(ans)