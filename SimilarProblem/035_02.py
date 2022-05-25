from collections import deque

n = int(input())
g = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

p = [-1] * n
t = []
q = deque([0])
while q:
    v = q.popleft()
    t.append(v)
    for nxt in g[v]:
        if p[nxt] != -1:
            continue
        p[nxt] = v
        g[nxt].remove(v)
        q.append(nxt)

dp_black = [1] * n
dp_white = [1] * n
mod = 10 ** 9 + 7
for i in t[::-1]:
    for j in g[i]:
        dp_black[i] *= dp_white[j]
        dp_white[i] *= dp_white[j] + dp_black[j]
        dp_black[i] %= mod
        dp_white[i] %= mod

print((dp_black[0] + dp_white[0]) % mod)