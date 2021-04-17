# まだ解けていません
from collections import deque
import sys
input = sys.stdin.readline

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def same(x,y):
    return find(x) == find(y)

def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    if x < y:
        x, y = y, x
    par[x] = y

h, w = map(int,input().split())
par = [i for i in range(h * w)]
q = int(input())
grid = [False] * (h * w) # 赤色 -> True, 白色 -> False
for i in range(q):
    a = list(map(int,input().split()))
    if a[0] == 1:
        grid[w * (a[1] - 1) + (a[2] - 1)] = True
    elif a[0] == 2:
        unite(w * (a[1] - 1) + (a[2] - 1), w * (a[3] - 1) + (a[4] - 1))
        if same(w * (a[1] - 1) + (a[2] - 1), w * (a[3] - 1) + (a[4] - 1)) and grid[w * (a[1] - 1) + (a[2] - 1)] and grid[w * (a[3] - 1) + (a[4] - 1)]:
            print("Yes")
        else:
            print("No")

print(par)
ans = [0] * (h * w)
for i in range(h * w):
    ans[find(i)] += 1
print(ans)
print(*grid)