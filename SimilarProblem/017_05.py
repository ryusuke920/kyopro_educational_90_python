n = int(input())
mod = 10 ** 9 + 7

ans = pow(10, n, mod)
no_1 = pow(9, n, mod)
no_19 = pow(8, n, mod)

print((ans - (no_1 * 2 - no_19)) % mod)