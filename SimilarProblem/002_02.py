from itertools import product
n = int(input())
a = list(map(int, input().split()))
ans = 10 ** 18
for i in product([0, 1], repeat = n):
    cnt = now = 0 # 現区間のXOR, 各区間のXOR
    for j in range(n):
        now |= a[j]
        if i[j] == 1: # bitが立つ <=> そこで一旦区切る
            cnt ^= now
            now = 0 # 区間のorを初期化
    cnt ^= now
    ans = min(ans, cnt)

print(ans)