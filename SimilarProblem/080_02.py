n = int(input())

mod = 10 ** 9 + 7
ans = pow(10, n, mod)
x = pow(9, n, mod) * 2
y = pow(8, n, mod)

print((ans - x + y) % mod)