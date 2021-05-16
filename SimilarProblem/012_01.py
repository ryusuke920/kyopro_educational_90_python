n, q = map(int,input().split())
par = [i for i in range(n + 1)]

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def same(x,y):
    return find(x) == find(y)

def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    par[x] = y

for i in range(q):
    p, a, b = map(int,input().split())
    if p == 0:
        unite(a, b)
    else:
        if same(a, b):
            print("Yes")
        else:
            print("No")