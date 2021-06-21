from bisect import bisect_left

def LIS(x):
    dp = [0] * n
    now = [0]
    for i in range(n):
        j = bisect_left(now, x[i])
        dp[i] = j
        if j == len(now):
            now.append(x[i])
        else:
            now[j] = x[i]
    return dp

n = int(input())
a = list(map(int, input().split()))

x = LIS(a) # 先頭からLIS
y = LIS(a[::-1]) # 末尾からLIS

ans = 0
for i in range(n):
    ans = max(ans, x[i] + y[-1 - i] - 1)

print(ans)