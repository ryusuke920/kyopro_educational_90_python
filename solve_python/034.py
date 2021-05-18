from collections import defaultdict
n, k = map(int,input().split())
a = list(map(int,input().split()))

cnt = defaultdict(int)
ans = 0 # 答え
l = 0 # 探す部分列の左端

for r in range(n):
    cnt[a[r]] += 1
    # 種類数がkを超えたら、k以下になるまでl（左端）を１つずつ右にシフトさせる
    while True:
        if len(cnt) <= k:
            break
        cnt[a[l]] -= 1
        if cnt[a[l]] == 0:
            del cnt[a[l]] # defaultdictからdeleteさせる
        l += 1
    ans = max(ans, r - l + 1)

print(ans)