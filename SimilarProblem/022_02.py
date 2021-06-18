import math
n = int(input())
a = list(map(int,input().split()))

ans = a[0]
for i in range(n - 1):
    ans = math.gcd(a[i + 1], ans)

print(ans)