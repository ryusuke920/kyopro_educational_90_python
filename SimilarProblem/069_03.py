n = int(input())
a = list(map(int, input().split()))

mod = 998244353
a.sort()
ans = 0
s = 0
for i in reversed(range(n - 1)):
    s *= 2
    s += a[i + 1]
    s %= mod
    ans += a[i] * s
    ans %= mod

for i in range(n):
    ans += a[i] ** 2
    ans %= mod

print(ans)