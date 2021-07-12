"""
最短距離はスヌークを大きくしていくほど、大きくなる
"""

N, P, K = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]

def pair_count_leq_p(x: int) -> int:
    "Xスヌークのときの選び方"
    dist = [[-1] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] == -1:
                dist[i][j] = x
            else:
                dist[i][j] = A[i][j]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    cnt = 0
    for i in range(N):
        for j in range(N):
            if i >= j: continue
            if dist[i][j] <= P:
                cnt += 1
    return cnt

INF = 10 ** 18
l_left, l_right = 0, INF
while l_right - l_left > 1:
    mid = (l_right + l_left) // 2
    if pair_count_leq_p(mid) <= K:
        l_right = mid
    else:
        l_left = mid

r_left, r_right = 0, INF
while r_right - r_left > 1:
    mid = (r_right + r_left) // 2
    if pair_count_leq_p(mid) < K:
        r_right = mid
    else:
        r_left = mid

if l_right == INF:
    print(0)
elif r_right == INF:
    print('Infinity')
else:
    print(r_right - l_right)