n, s = map(int,input().split())
a, b = [0] * n, [0] * n
for i in range(n):
    a[i], b[i] = map(int,input().split())

# dp[i][j] := i日目までで合計金額がj円にできるかどうか
dp = [[False] * (s + 1) for _ in range(n + 1)]
dp[0][0] = True

for i in range(n):
    for j in range(s + 1):
        if j - a[i] >= 0:
            dp[i + 1][j] |= dp[i][j - a[i]]
        if j - b[i] >= 0:
            dp[i + 1][j] |= dp[i][j - b[i]]

if not dp[n][s]:
    exit(print("Impossible"))

ans = ""
for i in reversed(range(n)):
    Bool = True
    if s - a[i] >= 0:
        if dp[i][s - a[i]] == True:
            ans += "A"
            s -= a[i]
            Bool = False
    if s - b[i] >= 0 and Bool:
        if dp[i][s - b[i]] == True:
            ans += "B"
            s -= b[i]

print(ans[::-1])