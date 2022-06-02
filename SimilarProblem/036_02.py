h, w, k = map(int, input().split())
S = [list(input()) for _ in range(h)]

# 前処理
num = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if S[i][j] == 'x':
            num[i][j] = -1
        else:
            if j == 0:
                num[i][j] = 1
            else:
                if num[i][j - 1] == -1:
                    num[i][j] = 1
                else:
                    num[i][j] = num[i][j - 1] + 1

ans = 0
for i in range(h):
    for j in range(w):
        if S[i][j] == 'x':
            continue
        ma = []
        ma.append((i + k - 1, j))
        ma.append((i - (k - 1), j))
        ma.append((i, j + k - 1))
        ma.append((i, j - (k - 1)))
        bool = True
        for y, x in ma:
            if not (0 <= x < w and 0 <= y < h):
                bool = False
                break

        if bool:
            check = True

            for up in range(k):
                y = i - k + up + 1
                left, right = max(0, j - up), j + up
                s = num[y][left]
                t = num[y][right]

                if t - s + 1 != 2 * up + 1 or S[y][left] == 'x' or S[y][right] == 'x':
                    check = False
         
            for down in range(k):
                y = i + k - down - 1
                left, right = max(0, j - down), j + down
                s = num[y][left]
                t = num[y][right]

                if t - s + 1 != 2 * down + 1 or S[y][left] == 'x' or S[y][right] == 'x':
                    check = False

            if check:
                ans += 1

print(ans)