from collections import Counter
n = int(input())
a = list(map(int,input().split()))

for i in range(n - 1):
    a[i + 1] += a[i]
a = [0] + a

cnt = Counter(a).most_common()

ans = 0
for i, j in cnt:
    ans += (j - 1) * j // 2

print(ans)