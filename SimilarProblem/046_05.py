s = list(map(int,list(input())))[::-1]
s = [0] + s
mod = 2019
for i in range(len(s) - 1):
    s[i + 1] *= pow(10, i, mod)
    s[i + 1] %= mod

# 累積和を取る
for i in range(len(s) - 2):
    s[i + 2] += s[i + 1]
    s[i + 2] %= mod

#print(s)
# [l, r] のとき、 S_{l-1} ≡ S_{r} が成り立てば良い
cnt = [0] * mod
for i in range(len(s)):
    cnt[s[i]] += 1

ans = 0
for i in range(mod):
    ans += cnt[i] * (cnt[i] - 1) // 2

print(ans)
