import sys
input = sys.stdin.readline
n, q = map(int,input().split())
s, t, x, y, z = [0] * n, [0] * n, [0] * q, [0] * q, [0] * q

for i in range(n):
    s[i], t[i] = map(int,input().split())

for i in range(q):
    x[i], y[i], z[i] = map(int,input().split())

for i in range(q):
    ans = 0
    for j in range(n):
        if s[j] >= x[i] and t[j] >= y[i] and s[j] + t[j] >= z[i]:
            ans += 1
    print(ans)