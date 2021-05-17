n, y = map(int,input().split())
# 合計でn枚
for i in range(0, 2001):# 10000円の枚数
    for j in range(0, 2001):# 5000円の枚数
        k = n - (i + j)# 1000円の枚数
        if k >= 0 and 10000 * i + 5000 * j + 1000 * k == y:
            exit(print(i, j, k))
print(-1, -1, -1)