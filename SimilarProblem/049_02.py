# 最小全域木（プリム法）
from heapq import heappop, heappush, heapify

n, m = map(int,input().split())
c = [int(input()) for _ in range(n)]

g = [[] for _ in range(n)]
for _ in range(m):
    a, b, r = map(int,input().split())
    g[a].append((r, b))
    g[b].append((r, a))

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