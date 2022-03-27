n = int(input())
a = sorted(list(map(int, input().split())))

ans = 0
for i in range(n - 1):
    ans += (a[i + 1] - a[i]) * (i + 1) * (n - i - 1)
print(ans)