"""
（与式） = |Xi - Xj| + |Yi - Yj|
    = max(Xi - Xj, Xj - Xi) + max(Yi - Yj, Yj - Yi)
    = max((Xi - Xj) + (Yi - Yj), (Xi - Xj) + (Yj - Yi), (Xj - Xi) + (Yi - Yj), (Xj - Xi) + (Yj - Yi))
    = max((Xi + Yi) - (Xj + Yj), (Xi - Yi) - (Xj - Yj), -{(Xi - Yi) - (Xj - Yj)}, -{(Xi + Yi) - (Xj + Yj)})
    = max(|(Xi + Yi) - (Xj + Yj)|, |(Xi - Yi) - (Xj - Yj)|)

ここで、
Zi = Xi + Yi
Wi = Xi - Yi
と置き換えると、

（与式）= max(|Zi - Zj|, |Wi - Wj|)
ここで i を固定すると、

（与式）= max(Zi - min(Zj), max(Zj) - Zi, Wi - min(Wj), max(Wj) - Wi)
となるので、

各クエリ毎の点を(Xi, Yi)と見なせば、O(1)でクエリを処理することが可能
※前処理として、min(Zj), max(Zj), min(Wj), max(Wj)をO(N)で求める
"""

n, q = map(int,input().split())
X, Y = [0] * n, [0] *  n

min_Zj, max_Zj, min_Wj, max_Wj = 10 ** 18, 0, 10 ** 18, 0

for i in range(n):
    X[i], Y[i] = map(int,input().split())
    min_Zj = min(min_Zj, X[i] + Y[i])
    max_Zj = max(max_Zj, X[i] + Y[i])
    min_Wj = min(min_Wj, X[i] - Y[i])
    max_Wj = max(max_Wj, X[i] - Y[i])

for _ in range(q):
    Q = int(input())
    Q -= 1
    Zi = X[Q] + Y[Q]
    Wi = X[Q] - Y[Q]
    print(max(Zi - min_Zj, max_Zj - Zi, Wi - min_Wj, max_Wj - Wi))