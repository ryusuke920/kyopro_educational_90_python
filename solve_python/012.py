import sys
input = sys.stdin.readline

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def same(x, y):
    return find(x) == find(y)

def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    if x < y:
        x, y = y, x
    par[x] = y

h, w = map(int,input().split())
q = int(input())

par = [i for i in range(h * w + 2)]
grid = [[False] * (w + 2) for _ in range(h + 2)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)] # ４方向に対する変化量

for i in range(q):
    a = list(map(int,input().split()))
    if a[0] == 1:
        grid[a[1]][a[2]] = True
        for dy, dx in d:
            if grid[a[1] + dy][a[2] + dx] == True: # 周囲４方向が塗られていれば、連結させる
                unite((a[1] + dy - 1) * w + (a[2] + dx), (a[1] - 1) * w + a[2])
    elif a[0] == 2: # 連結している & 2つのマスが赤色になっていればYes
        if same((a[1] - 1) * w + a[2], (a[3] - 1) * w + a[4]) and grid[a[1]][a[2]] and grid[a[3]][a[4]]:
            print("Yes")
        else:
            print("No")