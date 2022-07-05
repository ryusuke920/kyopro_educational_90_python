from math import gcd

def cross3(a: int, b: int, c: int) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def convex_hull(a: list) -> list:
    a.sort()
    q = []
    len_ = len(a)

    for p in a:
        while len(q) > 1 and cross3(q[-1], q[-2], p) > 0:
            q.pop()
        q.append(p)

    t = len(q)

    for i in range(len_ - 2, -1, -1):
        p = a[i]
        while len(q) > t and cross3(q[-1], q[-2], p) > 0:
            q.pop()
        q.append(p)

    return q


n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
convex = convex_hull(xy)

'''
ピックの定理
S = i + b / 2 - 1

i := 多角形の内部にある格子点の個数
b := 辺上にある格子点の個数

i = S - b / 2 + 1
'''

s = 0 # 多角形の面積
b = 0 # 辺上にある格子点の個数
for i in range(len(convex) - 1):
    x_i, y_i = convex[i]
    x_j, y_j = convex[i + 1]
    s += (x_i - x_j) * (y_i + y_j)
    b += gcd(abs(x_i - x_j), abs(y_i - y_j))

s = abs(s) // 2

i = s - b // 2 + 1 # 多角形の内部にある格子点の個数

print(i + b - n)