n, q = map(int,input().split())
a = list(map(int,input().split()))

b = [a[i + 1] - a[i] for i in range(n - 1)] # 階差数列を記録する配列
now = sum(abs(i) for i in b) # 現時点での不便さ

for i in range(q):
    l, r, v = map(int,input().split())
    if l > 1:
        l -= 2
        now -= abs(b[l])
        b[l] += v
        now += abs(b[l])
    if r < n:
        r -= 1
        now -= abs(b[r])
        b[r] -= v
        now += abs(b[r])
    print(now)