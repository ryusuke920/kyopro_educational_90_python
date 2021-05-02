from collections import deque
q = int(input())
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False # 便宜上false判定にしてる
    is_prime[1] = False # 便宜上false判定にしてる
    for i in range(2, n + 1):
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

x = primes(10 ** 5) # 素数の全列挙
l = len(x) # 素数の数

num = [0] * (10 ** 5 + 1) # i番目までに素数かどうかの判定
x = deque(x)
for i in range(1, 10 ** 5 + 1):
    if len(x) == 0: break
    a = x.popleft()
    num[a] = 1

ans = [0] * len(num) # 2017に似た数の累積和　＆　判定
ans[3] = 1
for i in range(5, len(num), 2):
    if num[i] == 0 or num[(i + 1) // 2] == 0 or (num[(i + 1) // 2]) % 2 == 0:
        ans[i] += ans[i - 2]
    else:
        ans[i] += 1
        ans[i] += ans[i - 2]

for i in range(q): # 各クエリごとに対する処理
    l, r = map(int,input().split())

    if ans[l] != ans[l - 2]:
        left = 1
    else:
        left = 0
    
    right = ans[r] - ans[l] + left
    
    print(right)