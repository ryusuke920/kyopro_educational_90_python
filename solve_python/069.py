n, k = map(int,input().split())
mod = 10 ** 9 + 7
if n == 1:
    print(k)
else:
    ans = k * (k - 1) * pow(k - 2, n - 2, mod)
    print(ans % mod)