from collections import defaultdict

n, k, q = map(int, input().split())

d = defaultdict(int)
for _ in range(q):
    a = int(input())
    d[a] += 1

for i in range(n):
    if k - q + d[i + 1] >= 1:
        print('Yes')
    else:
        print('No')