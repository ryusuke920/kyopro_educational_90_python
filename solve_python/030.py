def primes(n, k):
    if k == 1:
        exit(print(n - 2 + 1)) # 2 ~ N の全てが条件を満たす
    
    is_prime = [True] * (n + 1)
    num = [0] * (n + 1)
    for i in range(2, n + 1):
        if is_prime[i] != False: # 素数でなければ調和級数で全探索する
            for j in range(i, n + 1, i):
                is_prime[j] = False # 合成数になるのでFalseに
                num[j] += 1
    ans = 0
    for i in num[1:]:
        if i >= k: ans += 1
    return print(ans)

n, k = map(int,input().split())
primes(n, k)