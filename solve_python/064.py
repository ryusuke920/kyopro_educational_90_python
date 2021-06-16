n, q = map(int,input().split())
a = list(map(int,input().split()))
b = []
for i in range(n - 1):
    b.append(a[i + 1] - a[i])

for i in range(q):
    l, r, v = map(int,input().split())

print(b)