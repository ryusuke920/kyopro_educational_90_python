h,w = map(int,input().split())
s = [list(input()) for _ in range(h)]
l = [[0] * w for _ in range(h)] # 横
u = [[0] * w for _ in range(h)] # 縦

# 横方向を調べる
for i in range(h):
    for j in range(w):
        if s[i][j] == "#": continue
        if j == 0:
            l[i][j] = 1
        else:
            l[i][j] += l[i][j - 1] + 1

# 横方向の最大の累積和
for i in range(h):
    for j in range(w):
        if j == 0 or l[i][-j - 1] == 0: continue
        l[i][-j - 1] = max(l[i][-j - 1], l[i][-j])

# 縦方向を調べる
for i in range(w):
    for j in range(h):
        if s[j][i] == "#": continue
        if j == 0:
            u[j][i] = 1
        else:
            u[j][i] += u[j - 1][i] + 1

# 縦方向の最大の累積和
for i in range(w):
    for j in range(h):
        if j == 0 or u[-j - 1][i] == 0: continue
        u[-j - 1][i] = max(u[-j - 1][i], u[-j][i])

# 縦と横の最大値の和をとる
ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, l[i][j] + u[i][j] - 1)

print(ans)