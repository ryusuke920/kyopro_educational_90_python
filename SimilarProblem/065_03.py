def combination(n, k):
    nCk = under = top = 1

    for i in range(2, k + 1):
        under *= i

    for i in range(k):
        top *= (n - i)

    nCk = top // under

    return nCk

print(combination(int(input()) - 1, 11))