import sys
input = sys.stdin.readline
from itertools import permutations
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
m = int(input())
x = [list(map(int,input().split())) for _ in range(m)]

grid = [[True] * n for _ in range(n)]
# 仲の悪い組だけFalseにする
for i in range(m):
    grid[x[i][0] - 1][x[i][1] - 1] = False
    grid[x[i][1] - 1][x[i][0] - 1] = False

ans = 10 ** 18

for i in permutations(range(n)):
    Bool = True
    for j in range(n - 1):
        if not grid[i[j]][i[j + 1]]:
            Bool = False
            break

    cnt = 0 # リレーが可能な時の合計時間
    if Bool:
        for j in range(n):
            cnt += a[i[j]][j]
        ans = min(ans, cnt)

if ans == 10 ** 18:
    print(-1)
else:
    print(ans)