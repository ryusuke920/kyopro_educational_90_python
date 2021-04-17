n = int(input())
h = [0]*n
s = [0]*n
for i in range(n):
    h[i], s[i] = map(int,input().split())

def is_ok(x):
    l = []
    for i in range(n):
        l.append((x - h[i])//s[i]) # この時間までに割らなきゃいけない
    l.sort() # 小さいものから割る
    for j in range(n):
        if (l[j] < j):
            return False # アウトー
    return True

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print (meguru_bisect(0, 10**18))