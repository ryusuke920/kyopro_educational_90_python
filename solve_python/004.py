h, w = map(int,input().split())
a = []
for i in range(h):
    a.append(list(map(int,input().split())))
ans = [[0] * w for _ in range(h)]

# 縦の列ごとに合計を前計算する
y = [0] * w
for i in range(w):
    cnt = 0
    for j in range(h):
        cnt += a[j][i]
    y[i] = cnt

# 縦の列ごとに合計を前計算する
x = [0] * h
for i in range(h):
    cnt = 0
    for j in range(w):
        cnt += a[i][j]
    x[i] = cnt

for i in range(h):
    for j in range(w):
        ans[i][j] = (x[i] + y[j]) - a[i][j]

for i in range(h):
    print(*ans[i])