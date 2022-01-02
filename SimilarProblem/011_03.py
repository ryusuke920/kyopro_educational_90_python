n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]

g1, g2 = [], []
for i in range(n):
    a, b = ab[i]
    if a < b:
        g1.append((a, b))
    else:
        g2.append((a, b))

g1.sort(key=lambda x: x[0])
g2.sort(key=lambda x: -x[1])

ans = 0
high = 0
for a, b in g1:
    high += a
    ans = max(ans, high)
    high -= b

for a, b in g2:
    high += a
    ans = max(ans, high)
    high -= b

print(ans)