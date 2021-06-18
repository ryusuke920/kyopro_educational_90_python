from math import gcd
k = int(input())
ans = 0
for a in range(1, k + 1):
    for b in range(1, k + 1):
        ab = gcd(a,b)
        for c in range(1, k + 1):
            ans += gcd(ab, c)
print(ans)