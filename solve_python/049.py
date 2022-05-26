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

n, m = map(int,input().split())
item = [list(map(int, input().split())) for _ in range(m)]

uf = UnionFind(n + 1)
item.sort(key=lambda x: x[0])

ans = 0
for c, l ,r in item:
    l -= 1
    if uf.same(l, r):
        continue
    uf.merge(l, r)
    ans += c

par = set()
for i in range(n + 1):
    par.add(uf.leader(i))

print(ans) if len(par) == 1 else print(-1)