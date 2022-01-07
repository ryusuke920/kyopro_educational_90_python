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

mod = 10 ** 9 + 7
n = int(input())
k = int(input())
print(combination(n + k - 1, k))