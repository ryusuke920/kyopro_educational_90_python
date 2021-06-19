n = int(input())
x, y = [0] * n, [0] * n
for i in range(n):
    x[i], y[i] = map(int,input().split())

x.sort()
y.sort()
if n % 2 == 0:
    mid_x, mid_y = (x[n // 2 - 1] + x[n // 2]) // 2, (y[n // 2 - 1] + y[n // 2]) // 2
else:
    mid_x, mid_y = x[n // 2], y[n // 2]

ans = 0
for i in range(n):
    ans += abs(mid_x - x[i]) + abs(mid_y - y[i])
print(ans)