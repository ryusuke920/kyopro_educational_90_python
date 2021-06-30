h, w = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]
b = [list(map(int,input().split())) for _ in range(h)]
c = [[0] * w for _ in range(h)]

# それぞれのマスで何回足したりひいたりする必要があるかを求めたいので差を取る
for i in range(h):
    for j in range(w):
        c[i][j] = b[i][j] - a[i][j]

ans = 0
for i in range(h - 1):
    for j in range(w - 1):
        c[i][j + 1] -= c[i][j]
        c[i + 1][j] -= c[i][j]
        c[i + 1][j + 1] -= c[i][j]
        ans += abs(c[i][j])
        c[i][j] = 0

for i in range(h):
    for j in range(w):
        if c[i][j] != 0:
            exit(print("No"))

print("Yes")
print(ans)