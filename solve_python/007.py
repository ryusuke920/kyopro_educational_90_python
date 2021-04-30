from bisect import bisect_left
n = int(input())
a = list(map(int,input().split()))
q = int(input())
b = [int(input()) for _ in range(q)]
a.sort() # 昇順にソートし、２分探索が使えるようにする

for i in range(q):
    x = bisect_left(a, b[i])
    if x == 0: # １番小さい場合は配列Aの最小値とb[i]との差を取る
        print(a[0] - b[i])
    elif x == n: # 配列外参照になってしまうので、b[i]と配列Aの最小値との差をとる
        print(b[i] - a[-1])
    else:
        print(min(b[i] - a[x - 1], a[x] - b[i]))