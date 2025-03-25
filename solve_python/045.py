import sys
input = sys.stdin.readline

def main() -> None:
    N, K = map(int, input().split())
    XY = [tuple(map(int, input().split())) for _ in range(N)]

    dist = [[0]*N for _ in range(N)]
    for i in range(N - 1):
        for j in range(i + 1, N):
            dist[i][j] = (XY[i][0] - XY[j][0])**2 + (XY[i][1] - XY[j][1])**2
            dist[j][i] = dist[i][j]

    cost = [0]*(1 << N)
    for i in range(1, 1 << N):
        for j in range(1, N):
            if (i >> j) & 1 == 0:
                continue
            for k in range(j):
                if (i >> k) & 1 == 1:
                    cost[i] = max(cost[i], dist[j][k])

    INF = 10**18
    # dp[i][bit] := i 個のグループに分けた時既に決まっている bit 列
    dp = [[INF]*(1 << N) for _ in range(K + 1)]
    dp[0][0] = 0
    for i in range(1, K + 1):
        for j in range(1, 1 << N):
            k = j
            while k != 0:
                dp[i][j] = min(dp[i][j], max(dp[i - 1][j - k], cost[k]))
                k = (k - 1) & j

    print(dp[K][(1 << N) - 1])


if __name__ == "__main__":
    main()