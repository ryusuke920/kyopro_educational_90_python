def main():
    import sys
    input = sys.stdin.readline
    from collections import deque

    h, w = map(int,input().split())
    sy, sx = map(int,input().split())
    gy, gx = map(int,input().split())
    sy, sx = sy - 1, sx - 1
    gy, gx = gy - 1, gx - 1

    grid = []
    for _ in range(h):
        s = list(input())
        grid.append(s)

    INF = 10 ** 18
    dist = [INF] * (h * w * 4)

    # 障害物で通れない場所を探す（距離をマイナスにしておく）
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "#":
                for k in range(4):
                    dist[i * w * 4 + j * 4 + k] = -1

    q = deque()

    # (y, x)座標・向いている向き
    for i in range(4):
        q.append((sy, sx, i))

    # スタート地点は距離０で行ける
    for i in range(4):
        dist[sy * w * 4 + sx * 4 + i] = 0

    d = ((0, 1), (1, 0), (-1, 0), (0, -1)) # (y, x)方向への移動できる範囲
    while q:
        vy, vx, r = q.popleft() # 今いる（y, x）座標・向いている方向

        for i, (dy, dx) in enumerate(d):
            
            # 範囲外は調べない
            if not (0 <= vy + dy <= h - 1 and 0 <= vx + dx <= w - 1): continue

            # 行く先が障害物であれば調べない
            if dist[(vy + dy) * w * 4 + (vx + dx) * 4 + i] == -1: continue

            if i == r: # 向きを変えない場合（コストがかからない）
                if dist[(vy + dy) * w * 4 + (vx + dx) * 4 + i] > dist[vy * w * 4 + vx * 4 + r]:
                    dist[(vy + dy) * w * 4 + (vx + dx) * 4 + i] = dist[vy * w * 4 + vx * 4 + r]
                    q.appendleft((vy + dy, vx + dx, i)) # 先頭に追加する
            elif i != r: # 向きを変える場合（コストが１かかる）
                if dist[(vy + dy) * w * 4 + (vx + dx) * 4 + i] > dist[vy * w * 4 + vx * 4 + r] + 1:
                    dist[(vy + dy) * w * 4 + (vx + dx) * 4 + i] = dist[vy * w * 4 + vx * 4 + r] + 1
                    q.append((vy + dy, vx + dx, i)) # 末尾に追加する

    #print(dist)
    # ４方向に対する最小値が答え
    ans = INF
    for i in range(4):
        if dist[gy * w * 4 + gx * 4 + i] == -1: continue
        ans = min(ans, dist[gy * w * 4 + gx * 4 + i])
    print(ans)

if __name__ == "__main__":
    main()