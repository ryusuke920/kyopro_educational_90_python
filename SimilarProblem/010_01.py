n, k = map(int,input().split())
a = [int(input()) for _ in range(n)]
num = sum(a[:k])
ans = num
for i in range(n - k):
    num += a[i + k] - a[i]
    ans = max(ans, num)
print(ans)