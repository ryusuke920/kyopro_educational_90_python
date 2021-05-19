n, a, b = map(int,input().split())

mod = 10 ** 9 + 7
ans = 0

nCa = 1
for i in range(a):
    nCa *= (n - i) * pow(i + 1, mod - 2, mod)
    nCa %= mod

nCb = 1
for i in range(b):
    nCb *= (n - i) * pow(i + 1, mod - 2, mod)
    nCb %= mod

ans = pow(2, n, mod) - (nCa + nCb) - 1
ans %= mod
print(ans)