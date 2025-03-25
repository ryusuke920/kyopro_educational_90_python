def calc(x1: int, y1: int, x2: int, y2: int) -> int:
    return (x1 - x2)**2 + (y1 - y2)**2


N, K = map(int, input().split())
X, Y = [0]*N, [0]*N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

INF = 10**20
# dp[i][j] := 点(Xj, Yj) を i 個のグループに分けた時の最小コスト
