n, q = map(int,input().split())
a = list(map(int,input().split()))

shift = 0 # シフトする回数はN周期であり、N回シフトしたら元の位置に戻ってくる
for i in range(q):
    t, x, y = map(int,input().split())
    x, y = x - 1, y - 1 # 0indexに変換する

    # シフトも含めたindexを決める（これもN周期）
    X = (x - shift) % n
    Y = (y - shift) % n

    if t == 1:
        a[X], a[Y] = a[Y], a[X]
    elif t == 2:
        shift += 1
        shift %= n
    elif t == 3:
        print(a[X])