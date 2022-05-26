class UnionFind:
    def __init__(self, n):
        self.n = n
        self.p = [-1] * n


    def leader(self, a):
        while self.p[a] >= 0:
            a = self.p[a]
        return a


    def merge(self, a, b):
        x = self.leader(a)
        y = self.leader(b)

        if x == y:
            return x

        if self.p[x] > self.p[y]:
            x, y = y, x

        self.p[x] += self.p[y]
        self.p[y] = x

        return x

    def same(self, a, b):
        return self.leader(a) == self.leader(b)

    def size(self, a):
        return -self.p[self.leader(a)]

n = int(input())
xy = [[i] + list(map(int, input().split())) for i in range(n)]

uf = UnionFind(n)
g = []

xy.sort(key=lambda x: x[1])
for i in range(n - 1):
    u, v, cost = xy[i][0], xy[i + 1][0], xy[i + 1][1] - xy[i][1]
    g.append((u, v, cost))

xy.sort(key=lambda x: x[2])
for i in range(n - 1):
    u, v, cost = xy[i][0], xy[i + 1][0], xy[i + 1][2] - xy[i][2]
    g.append((u, v, cost))

g.sort(key=lambda x: x[2])
ans = 0
for u, v, cost in g:
    if uf.same(u, v):
        continue
    uf.merge(u, v)
    ans += cost

print(ans)