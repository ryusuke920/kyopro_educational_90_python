import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int,input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

def dfs(u: int, par: int) -> None:
    for i in g[u]:
        if i == par: continue
        dfs(i, u)
        size[u] += size[i]

size = [1] * n
dfs(0, -1)

ans = 0
for i in range(n):
    ans += size[i] * (n - size[i])

print(ans)