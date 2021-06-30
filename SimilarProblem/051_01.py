from bisect import bisect_right
from itertools import product
n, t = map(int,input().split())
a = list(map(int,input().split()))

left = [0]
for i in product([0,1], repeat = min(20, n)):
    cnt = 0
    for j in range(min(20, n)):
        if i[j] == 1:
            cnt += a[j]
    left.append(cnt)
left = list(set(left))
left.sort()

right = [0]
for i in product([0,1], repeat = max(0, n - 20)):
    cnt = 0
    for j in range(max(0, n - 20)):
        if i[j] == 1:
            cnt += a[j + 20]
    right.append(cnt)
right = list(set(right))
right.sort()

ans = 0
for i in range(len(left)):
    if left[i] > t: continue
    j = right[bisect_right(right, t - left[i]) - 1]
    ans = max(ans, left[i] + j)

print(ans)