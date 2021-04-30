import sys
input = sys.stdin.readline
n = int(input())

graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int,input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

group = [[], []]
q = [[0, -1, 0]] # 今いる頂点・一つ前の頂点・組(0 or 1)
while q:
    v, past, color = q.pop()
    group[color].append(v + 1) # 0indexなので +1 をする
    for i in graph[v]: # 今いる頂点に隣接しているノードを見る
        if i == past: continue
        q.append([i, v, color ^ 1])

if len(group[0]) >= n // 2:
    print(*group[0][: n // 2])
else:
    print(*group[1][: n // 2])