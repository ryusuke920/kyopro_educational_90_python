import math
a, b, c = map(int,input().split())
gcd_ab = math.gcd(a, b)
gcd_abc = math.gcd(gcd_ab, c)

ans = (a // gcd_abc - 1) + (b // gcd_abc -  1) + (c // gcd_abc - 1)
print(ans)