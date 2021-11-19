# 最小全域木（プリム法）
from heapq import heappop, heappush, heapify

n, m = map(int,input().split())

g = [[] for _ in range(n)]
for _ in range(m):
    u, v, cost = map(int,input().split())
    g[u].append((cost, v))
    g[v].append((cost, u))

visited = [0] * n
connection = 0
q = []
q.append((0, 0))
heapify(q)

ans = 0
while q:
    cost, v = heappop(q)
    if visited[v]: continue

    visited[v] = 1
    connection += 1
    ans += cost

    for nxt in g[v]:
        heappush(q, nxt)
    
    if connection == n:
        break

print(ans)