from heapq import heappush, heappop
n, m = map(int,input().split())
a = [0] * m
b = [0] * m
for i in range(m):
    a[i], b[i] = map(int,input().split())

def dijkstra(s, num): # 始点・取り除く辺のindex番号
    graph_removed = [[] for _ in range(n)] # １つの辺を除いた隣接行列
    for i in range(m):
        if i != num:
            graph_removed[a[i] - 1].append(b[i] - 1)
            graph_removed[b[i] - 1].append(a[i] - 1)
    dist = [10 ** 18] * n
    check = [False] * n
    dist[s] = 0
    q = [(0, s)] # 距離・ノード
    while q:
        v = heappop(q)[1] # 今いるノード
        if check[v]: continue
        check[v] = True
        for i in graph_removed[v]: # 先のノード
            if check[i] != False: continue
            if dist[i] <= dist[v] + 1: continue
            dist[i] = dist[v] + 1
            heappush(q, (dist[i], i))
    return dist

ans = 0 # 取り除いたほうが良い辺の数
for i in range(m):
    x = dijkstra(0, i) # 始点は常に0からスタートとする（便宜上）・取り除くエッジのindex
    if 10 ** 18 in x: # 更新されてないってことは除いた辺なしではたどり着けない！！
        ans += 1
print(ans)