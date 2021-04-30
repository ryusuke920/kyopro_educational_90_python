import sys
from bisect import bisect_left
from math import atan2, degrees
input = sys.stdin.readline

n = int(input())
xy = [tuple(map(int,input().split())) for _ in range(n)]

ans = 0
for i, (x, y) in enumerate(xy):
    num = []
    for j, (xx, yy) in enumerate(xy):
        if i == j: continue
        Y, X = yy - y, xx - x
        num.append(degrees(atan2(Y, X)) % 360) # 負の角度もあるのでmod360をとる
    num.sort()

    for j in range(len(num)):
        #現在の角度 >= 180 のとき +180 % 360をすると、理想値が得られる
        #例) 225°のとき、180°に近くなるのは、(225 + 180) % 360 = 45°になる
        want = (num[j] + 180) % 360
        
        # 欲しい角度に一番近い値を二部探索（上限はn - 2）
        cnt = min(bisect_left(num, want), n - 2)

        # 理想値に１番近くて小さいもの、１番近くて大きいもの
        a = min(abs(num[j] - num[cnt]), 360 - abs(num[j] - num[cnt]))
        b = min(abs(num[j] - num[cnt - 1]), 360 - abs(num[j] - num[cnt - 1]))

        ans = max(ans, a, b)
print(ans)