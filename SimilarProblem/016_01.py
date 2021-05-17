k, s = map(int,input().split())
cnt = 0
for i in range(k + 1):
    for j in range(k + 1):
        l = s - (i + j)
        if i + j + l == s and l >= 0 and l <= k and i <= k and j <= k:
            cnt += 1
print(cnt)