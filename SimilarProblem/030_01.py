import math
n = int(input())
a = list(map(int,input().split()))
x = math.gcd(a[0], a[1])
for i in range(n - 2):
    x = math.gcd(x, a[i + 2])

if x != 1:
    exit(print("not coprime "))

# 10^6以下の素数は78498個なのでそれ以上ある場合は必ず重複した素因数を持つ（鳩の巣原理）
if len(set(a)) >= 78499:
    exit(print("setwise coprime"))

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr

ans = []
for i in range(n):
    ans.append(factorization(a[i]))
num = {}
for i in ans:
    for j in range(len(i)):
        if i[j][0] not in num or i[j][0] == 1:
            num[i[j][0]] = 1
        else: exit(print("setwise coprime"))

print("pairwise coprime")