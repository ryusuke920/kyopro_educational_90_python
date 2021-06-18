def dfs(y, x, a, b, check):
    ans = 0
    if y == h:
        ans = 1
    elif x == w:
        ans = dfs(y + 1, 0, a, b, check)
    elif check[y][x] == True:
        ans = dfs(y, x + 1, a, b, check)
    else:
        ans = 0
        check[y][x] = True
        if a > 0:
            # 横に行くパターン
            if 0 <= x < w - 1 and check[y][x + 1] == False:
                check[y][x + 1] = True
                ans += dfs(y, x + 1, a - 1, b, check)
                check[y][x + 1] = False
            # 縦に行くパターン
            if 0 <= y < h - 1 and check[y + 1][x] == False:
                check[y + 1][x] = True
                ans += dfs(y, x + 1, a - 1, b, check)
                check[y + 1][x] = False
        if b > 0:
            ans += dfs(y, x + 1, a, b - 1, check)
        check[y][x] = False
    return ans

h, w, A, B = map(int,input().split())
check = [[False] * w for _ in range(h)]
print(dfs(0, 0, A, B, check))