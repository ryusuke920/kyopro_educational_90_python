n = int(input())
a = list(map(int,input().split()))
r, m = [0] * n, [0] * n # 最大の累積和
r[0] = a[0]
d = a[0]
m[0] = a[0]

for i in range(n - 1):
    d += a[i + 1]
    r[i + 1] = r[i] + d

ch = 0
for i in range(n - 1):
    if a[i + 1] + ch > 0:
        m[i + 1] = m[i] + a[i + 1] + ch
        ch = 0
    else:
        m[i + 1] = m[i]
        ch += a[i + 1]

ans = 0
for i in range(n):
    if i == n - 1:
        ans = max(ans, r[i])
    else:
        ans = max(ans, r[i] + m[i])

print(ans)