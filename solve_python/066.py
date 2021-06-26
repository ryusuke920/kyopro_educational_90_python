# 期待値の線形性
n = int(input())
l, r = [0] * n, [0] * n
for i in range(n):
    l[i], r[i] = map(int,input().split())

ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        x = r[i] - l[i] + 1
        y = r[j] - l[j] + 1
        under = x * y
        for k in range(l[i], r[i] + 1):
            top = max(0, min(k - 1, r[j]) - l[j] + 1)
            ans += top / under

print(ans)