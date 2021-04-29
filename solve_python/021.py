import sys
input = sys.stdin.readline

def SCC(to, ot):
    # まだ通ってない -> -1, 行きに通った -> 0, 帰りに通った -> 1, dfsも済んだ -> 2
    check = [-1] * n
    q = []
    for i in range(n):
        if check[i] != -1: continue
        stack = [i]
        while stack:
            v = stack.pop()
            if check[v] == -1:
                check[v] = 0
                for j in to[v]:
                    if check[j] != -1: continue
                    stack.append(j)
            else:
                stack.pop()
                if check[v] == 0:
                    check[v] = 1
                    q.append(v)
        
    # 逆辺でdfs
    num = []
    while q:
        v = q.pop()
        if check[v] != 1: continue
        check[v] = 2
        now = [v]
        i = 0
        while i < len(now):
            v = now[i]
            for j in ot[v]:
                if check[j] == 2: continue
                check[j] = 2
                now.append(j)
            i += 1
        num.append(now)
    
    return num


n, m = map(int,input().split())
a, b = [0] * m, [0] * m

to = [[] for _ in range(n)]
ot = [[] for _ in range(n)]

for i in range(m):
    a[i], b[i] = map(int,input().split())
    to[a[i] - 1].append(b[i] - 1)
    ot[b[i] - 1].append(a[i] - 1)

ans = 0
for i in SCC(to, ot):
    cnt = len(i)
    ans += cnt * (cnt - 1) // 2

print(ans)