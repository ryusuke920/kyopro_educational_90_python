n = int(input())

fac = [1] * 110000
inv = [1] * 110000
mod = 10 ** 9 + 7

for i in range(1, 110000):
    fac[i] = fac[i - 1] * i % mod

inv[-1] = pow(fac[-1], mod - 2, mod)
for i in reversed(range(0, 110000)):
    inv[i - 1] = inv[i] * i % mod

def nCk(n: int, k: int):
    if k < 0 or n - k < 0: return 0
    return fac[n] * inv[n - k] % mod * inv[k] % mod

for k in range(1, n + 1):
    ans = 0
    for i in range(1, n + 1):
        p = n - (k - 1) * (i - 1)
        if p < i: break
        ans += nCk(p, i)
        ans %= mod
    print(ans)