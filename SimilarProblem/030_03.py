import math
n = int(input())
a = list(map(int,input().split()))

mod = 10 ** 9 + 7
ans = 0
lcm = a[0]

for i in range(1, n):
    lcm = lcm * a[i] // math.gcd(lcm, a[i])

for i in range(n):
    ans += lcm // a[i]

print(ans % mod)