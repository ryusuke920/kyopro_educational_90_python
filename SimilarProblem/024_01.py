n = int(input())
t, x, y = [0] * n, [0] * n, [0] * n
for i in range(n):
    t[i], x[i], y[i] = map(int,input().split())

time = t[0]
go = x[0] + y[0]
if time < go or time % 2 != go % 2:
    exit(print("No"))

for i in range(n - 1):
    time = t[i + 1] - t[i]
    go = abs(x[i + 1] - x[i]) + abs(y[i + 1] - y[i])
    if time < go or time % 2 != go % 2:
        exit(print("No"))

print("Yes")