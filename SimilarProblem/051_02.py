from itertools import product
from collections import Counter, defaultdict
n, x = map(int,input().split())
w = [int(input()) for _ in range(n)]

left = []
for i in product([0, 1], repeat = min(16, n)):
    cnt = 0
    for j in range(min(16, n)):
        if i[j] == 1:
            cnt += w[j]
    left.append(cnt)

right = []
for i in product([0, 1], repeat = max(0, n - 16)):
    cnt = 0
    for j in range(max(0, n - 16)):
        if i[j] == 1:
            cnt += w[j + 16]
    right.append(cnt)


dl, dr = defaultdict(int), defaultdict(int)

# 前半の方の出現回数をdict型にする
L = Counter(left).most_common()
for number, cnt in L:
    dl[number] = cnt

# 後半の方の出現回数をdict型にする
R = Counter(right).most_common()
for number, cnt in R:
    dr[number] = cnt

ans = 0
for number in dl.keys():
    ans += dl[number] * dr[x - number]
print(ans)