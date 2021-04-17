n = int(input())
a, b, c = map(int,input().split())
ans = 10 ** 9
for i in range(10 ** 4): # A円の硬貨の枚数
    for j in range(10 ** 4): # B円の硬貨の枚数
        k = n - (a * i + b * j) # C円で払わなければならない値段
        if k % c == 0 and k >= 0:
            ans = min(ans, i + j + k // c)
print(ans)