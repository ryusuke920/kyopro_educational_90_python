import sys
input = sys.stdin.readline

"SCC（Strongly Connected Component） := 強連結成分分解"
class SCC:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.rev_graph = [[] for _ in range(n)]
        self.labels = [-1] * n
        self.lb_cnt = 0

    def add_edge(self, v, nxt_v):
        self.graph[v].append(nxt_v)
        self.rev_graph[nxt_v].append(v)

    def build(self):
        self.post_order = []
        self.used = [False] * self.n
        for v in range(self.n):
            if not self.used[v]:
                self._dfs(v)
        for v in reversed(self.post_order):
            if self.labels[v] == -1:
                self._rev_dfs(v)
                self.lb_cnt += 1

    def _dfs(self, v):
        stack = [v, 0]
        while stack:
            v, idx = stack[-2:]
            if not idx and self.used[v]:
                stack.pop()
                stack.pop()
            else:
                self.used[v] = True
                if idx < len(self.graph[v]):
                    stack[-1] += 1
                    stack.append(self.graph[v][idx])
                    stack.append(0)
                else:
                    stack.pop()
                    self.post_order.append(stack.pop())

    def _rev_dfs(self, v):
        stack = [v]
        self.labels[v] = self.lb_cnt
        while stack:
            v = stack.pop()
            for nxt_v in self.rev_graph[v]:
                if self.labels[nxt_v] != -1:
                    continue
                stack.append(nxt_v)
                self.labels[nxt_v] = self.lb_cnt

    def construct(self):
        self.dag = [[] for i in range(self.lb_cnt)]
        self.groups = [[] for i in range(self.lb_cnt)]
        for v, lb in enumerate(self.labels):
            for nxt_v in self.graph[v]:
                nxt_lb = self.labels[nxt_v]
                if lb == nxt_lb:
                    continue
                self.dag[lb].append(nxt_lb)
            self.groups[lb].append(v)
        return self.dag, self.groups


n = int(input()) # ノード数
graph = [list(map(int,input().split())) for _ in range(n - 1)] # エッジの受け取り
scc = SCC(n) # Classを使えるようにする

for u, v in graph:
    scc.add_edge(u - 1, v - 1) # 有向グラフにする（0index）
scc.build()

q = int(input())
for _ in range(q):
    a, b = map(int,input().split())
    scc.add_edge(a - 1, b - 1)

    _,elems = scc.construct() # 閉路ずつの配列で帰ってくる
    print(a,b,elems)