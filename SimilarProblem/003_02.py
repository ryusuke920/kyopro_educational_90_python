import sys
n = int(input())
a = 1 # 最初の頂点
b = 2 # 始点と比べたい頂点
dist = [0] * 2 # 頂点1からiまでの距離とその頂点からの最大値
for i in range(n - 1):
    print("? {0} {1}".format(a, b + i))
    sys.stdout.flush()
    d = int(input())
    if dist[0] <= d:
        dist[0] = d
        num = b + i

b = 1 # 比べる頂点を初期化
for i in range(1, n + 1):
    if i == num: continue
    print("? {0} {1}".format(num, i))
    sys.stdout.flush()
    d = int(input())
    if dist[1] <= d:
        dist[1] = d
print("!",max(dist))