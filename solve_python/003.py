import sys 
input = sys.stdin.readline
from heapq import heappush, heappop

def dijkstra(s, g): # 始点・隣接グラフ
    INF = 10 ** 18
    check = [False] * n
    dist = [INF] * n
    dist[s] = 0
    q = [(0, s)] # 距離・ノード
    while q:
        node = heappop(q)[1] # 今いる所までの距離・そのノード
        if check[node]: continue
        check[node] = True
        for i in g[node]: # これから行く所までの距離・そのノード
            if check[i]: continue
            if dist[i] <= dist[node] + 1: continue
            dist[i] = dist[node] + 1
            heappush(q, [dist[i], i])
    return dist

n = int(input())
graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int,input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

zero_dis = dijkstra(0, graph) # 頂点１から端点（木の端）を求める
max_index = zero_dis.index(max(zero_dis)) # 端点のindex
ans = dijkstra(max_index, graph) # 端点からの最大距離

print(max(ans) + 1)