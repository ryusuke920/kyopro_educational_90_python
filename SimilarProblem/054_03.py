from heapq import heappush, heappop
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dijkstra(s, graph):
    INF = 10 ** 18
    dist = [INF] * (n + 6)
    dist[s] = 0
    check = [False] * (n + 6)
    q = [(0, s)]
    while q:
        v = heappop(q)[1]
        if check[v]: continue
        check[v] = True
        for i, j in graph[v]:
            if check[i] != False: continue
            if dist[i] <= dist[v] + j: continue
            dist[i] = dist[v] + j
            heappush(q, (dist[i], i))
    return dist

n, m = map(int,input().split())
Xab, Xac, Xbc = map(int,input().split())
s = input()

# 1, 2, 3, ..., n, Ain, Bin, Cin, Aout, Bout, Cout
g = [[] for _ in range(n + 6)]
for v, ch in enumerate(s):
    if ch == "A":
        g[v].append((n, 0))
        g[n + 3].append((v, 0))
    elif ch == "B":
        g[v].append((n + 1, 0))
        g[n + 4].append((v, 0))
    elif ch == "C":
        g[v].append((n + 2, 0))
        g[n + 5].append((v, 0))

# 有向グラフの追加
g[n].append((n + 4, Xab))
g[n].append((n + 5, Xac))
g[n + 1].append((n + 3, Xab))
g[n + 1].append((n + 5, Xbc))
g[n + 2].append((n + 3, Xac))
g[n + 2].append((n + 4, Xbc))

for i in range(m):
    a, b, c = map(int,input().split())
    g[a - 1].append((b - 1, c))
    g[b - 1].append((a - 1, c))

print(dijkstra(0, g)[n - 1])