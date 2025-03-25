v, e = map(int, input().split())

INF = 10 ** 18
g = [[INF] * v for _ in range(v)]
for _ in range(e):
    s, t ,d = map(int, input().split())
    g[s][t] = d

dp = [[INF] * v for _ in range(2 ** v)]
# dp[i][j] := 部分集合 i の順列の中で j が末項のうち、最も最適なコスト
dp[0][0] = 0

for s in range(2 ** v):
    for a in range(v):
        for b in range(v):
            # a -> b への path
            if (s >> b) & 1 == 1: continue
            if  (s >> a) & 1 == 0 and s != 0: continue
            dp[s | (1 << b)][b] = min(dp[s | (1 << b)][b], dp[s][a] + g[a][b])

print(dp[-1][0]) if dp[-1][0] != INF else print(-1)