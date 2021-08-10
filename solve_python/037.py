w, n = map(int,input().split())
# dp[i] := 香辛料w(mg)で作ることのできる価値の最大値
dp = [-1 for _ in range(w + 1)]
dp[0] = 0

for i in range(n):
    l, r, v = map(int,input().split())

    for j in reversed(range(w)):
        if dp[j] != -1:
            if j + l <= w:
                dp[j + l] = max(dp[j] + v, dp[j + l])
                if j + r < w:
                    dp[j + r] = max(dp[j] + v, dp[j + r])
                elif w <= j + r:
                    dp[w] = max(dp[j] + v, dp[w])
print(dp[w])