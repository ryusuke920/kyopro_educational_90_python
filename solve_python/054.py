from collections import deque
n, m = map(int,input().split())
g = [[] for  _ in range(n + m)]

# 論文の頂点をn+1, n+2, ... ,n + mとする 
for i in range(m):
    K = int(input())
    for R in map(int,input().split()):
        g[n + i].append(R - 1)
        g[R - 1].append(n + i)

dist = [-1] * (n + m)
dist[0] = 0
q = deque()
q.append(0)

while q:
    v = q.popleft()
    for i in g[v]:
        if dist[i] != -1: continue
        dist[i] = dist[v] + 1
        q.append(i)

for i in range(n):
    print(dist[i] // 2)