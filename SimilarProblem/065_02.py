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

x, y = map(int, input().split())

'''
a + 2b = x
2a + b = y

a = (2y - x) // 3
b = (2x - y) // 3
'''

mod = 10 ** 9 + 7
if (2 * y - x) % 3 == 0 and (2 * x - y) % 3 == 0:
    a = (2 * y - x) // 3
    b = (2 * x - y) // 3
    if a >= 0:
        print(combination(a + b, a))
    else:
        print(combination(a + b, b))
else:
    print(0)