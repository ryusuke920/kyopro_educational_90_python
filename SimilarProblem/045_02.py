N = int(input())
S = input()

d = {"J": 1 << 2, "O": 1 << 1, "I": 1 << 0}
# dp[i][j] := i 列目まで見た時の集合が j の時の組み合わせ
dp = [[0]*(1 << 3) for _ in range(N + 1)]
dp[0][d["J"]] = 1
mod = 10007
for i in range(N):
    # 今日の責任者
    people = d[S[i]]
    for last in range(1 << 3):
        for now in range(1 << 3):
            # 責任者は now に含まれなければいけない
            if (now & people) == 0:
                continue
            # 昨日の参加者の中に最低でも１人は今日参加する人がいなければならない
            if (last & now) == 0:
                continue
            dp[i + 1][now] += dp[i][last]
            dp[i + 1][now] %= mod

# 答えを求める
ans = 0
for j in range(1 << 3):
    ans += dp[N][j]
    ans %= mod
print(ans)