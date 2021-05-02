n, m = map(int,input().split()) # 宿場町の個数・旅の日付
dist = [int(input()) for _ in range(n - 1)] # 宿場町間の距離
mod = 10 ** 5

before, after = [0] * (n - 1), [0] * (n - 1) # 前からの累積和, 後ろからの累積和
before[0], after[0] = dist[0], dist[-1]
for i in range(n - 2):
    before[i + 1] += before[i] + dist[i + 1]
    after[i + 1] += after[i] + dist[-i - 2]
before = [0] + before + [0]
after = [0] + after + [0]
after = after[::-1]

ans = 0
now = 0 # 今いる宿場町
for _ in range(m):
    t = int(input())
    if t > 0:
        ans += before[now + t] - before[now]
    elif t < 0:
        ans += after[now + t + 1] - after[now + 1]
    now += t
print(ans % mod)