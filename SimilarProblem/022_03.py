import math
n = int(input())
a = list(map(int,input().split()))
l, r = [0], [0]

for i in range(n-1):
    #左から見ていく
    l.append(math.gcd(l[i], a[i]))
    #右から見ていく
    r.append(math.gcd(r[i], a[-1-i]))

r = r[::-1]
ans = 0
for i in range(n):
    ans = max(ans,math.gcd(l[i], r[i]))

print(ans)