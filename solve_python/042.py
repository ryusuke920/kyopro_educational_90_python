# https://twitter.com/mkawa2/status/1394443931564138500
# 河崎さんの解説ACさせていただきました。

k = int(input())
mod = 10 ** 9 + 7

# 桁和が9の倍数でなければ9の倍数にならない
if k % 9 != 0:
    exit(print(0))

dp = [1] * (k + 1)
for i in range(1, k):
    if i - 9 >= 0:
        dp[i + 1] = (dp[i] * 2 - dp[i - 9]) % mod
    else:
        dp[i + 1] = (dp[i] * 2) % mod

print(dp[k])