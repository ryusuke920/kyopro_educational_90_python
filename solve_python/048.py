n, k = map(int,input().split())
 
ab = []
ans = 0 # 全てのテストで満点取った合計
for _ in range(n):
    a, b = map(int,input().split())
    ans += a
    ab.append(a - b)
    ab.append(b)
 
ab.sort() # 昇順にする
for i in range(2 * n - k): # 減らさなければならない回数
    ans -= ab[i]
 
print(ans)