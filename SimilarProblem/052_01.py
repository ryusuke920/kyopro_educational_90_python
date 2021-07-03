a, b, c = map(int,input().split())
mod = 998244353
x = a * (a + 1) // 2
y = b * (b + 1) // 2
z = c * (c + 1) // 2
print((x * y * z) % mod)