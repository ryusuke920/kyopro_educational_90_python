n = int(input())
xy = [list(map(int,input().split())) for _ in range(n)]
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if (xy[j][1] - xy[i][1]) * (xy[k][0] - xy[j][0]) == (xy[k][1] - xy[j][1]) * (xy[j][0] - xy[i][0]):
                exit(print("Yes"))
print("No")