def combination(n, k):
    nCk = under = top = 1

    for i in range(2, k + 1):
        under *= i
        under %= mod

    for i in range(k):
        top *= (n - i)
        top %= mod

    nCk = top * pow(under, mod - 2, mod)

    return nCk % mod

n = int(input())

mod = 10 ** 9 + 7
ans = 0
for i in range(1, 700):
    # i個の長さで敷き詰める場合
    if 3 * i > n: break
    # n - 3 * i個をi個の袋に分ける
    num = n - 3 * i
    ans += combination(num + (i - 1), i - 1)
    ans %= mod

print(ans)