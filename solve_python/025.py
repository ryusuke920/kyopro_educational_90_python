def f(m): # f(m)の値を全て列挙する
    num = 1
    for i in range(len(str(m))):
        num *= int(str(m)[i])
    return num

def dfs(Fm, cnt):
    """
    m = B + f(m) > n: break (f(m) := Fm と定義してる)
    """
    if Fm + b > n:
        return None
    Fm_list.add(Fm)
    for prime in range(cnt, 4): # 素数をかけていく（樹形図を書くと理解しやすい）
        dfs(Fm * primes[prime], prime)

n, b = map(int,input().split())

if n < b: # n - f(n) < b であれば全ての n で条件を満たさない
    exit(print(0))

Fm_list = set() # f(m)の候補としてあり得そうなものを格納する配列
Fm_list.add(0)
primes = [2, 3, 5, 7] # f(m)の取りうる4つの素因数
dfs(1, 0)

ans = 0
for fm in Fm_list:
    if f(fm + b) == fm:
        ans += 1

print(ans)