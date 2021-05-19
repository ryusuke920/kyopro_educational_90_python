"""
〜segfuncの使い方について〜
update(k, x): k番目の要素をxに更新する
query(l, r): [l, r)（l <= k < r の区間）から値kを取得する
"""
def segfunc(x: int, y: int) -> int:
    "ここで求めたい処理を行う, max(x, y) や x ^ y など"
    return max(x, y)

"""
〜単位元の一覧について〜
最小値：float("inf")
最大値：-float("inf")
XOR：0
区間和：0
区間積：1
最大公約数：0
"""
ide_ele = -float("inf") # 初期値（単位元）の設定

class SegTree:
    def __init__(self, segfunc, init_val, ide_ele):
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 2 ** n.bit_length()
        self.seg = [self.ide_ele] * 2 * self.num
        for i in range(n):
            self.seg[i+self.num - 1] = init_val[i]
        for i in range(self.num - 2, -1, -1):
            self.seg[i] = self.segfunc(self.seg[2 * i + 1], self.seg[2 * i + 2])

    def update(self, k, x):
        k += self.num - 1
        self.seg[k] = self.segfunc(self.seg[k], x)
        while k:
            k = (k - 1) // 2
            self.seg[k] = self.segfunc(self.seg[k * 2 + 1], self.seg[k * 2 + 2])

    def query(self, l, r):
        " l は0index, r は1index"
        if r <= l:
            return self.ide_ele
        l += self.num - 1
        r += self.num - 2
        res = self.ide_ele
        while r - l > 1:
            if l & 1 == 0:
                res = self.segfunc(res, self.seg[l])
            if r & 1 == 1:
                res = self.segfunc(res, self.seg[r])
                r -= 1
            l = l // 2
            r = (r - 1) // 2
        if l == r:
            res = self.segfunc(res, self.seg[l])
        else:
            res = self.segfunc(res, self.segfunc(self.seg[l], self.seg[r]))
        return res

w, n = map(int,input().split()) # 配列の長さ・クエリ数
dp = [[0] * (w + 1) for _ in range(n + 1)]
#seg = SegTree(segfunc, dp, ide_ele) # オブジェクトの作成

# dp[i] := i(mg)を利用して作れる最大の価値

l, r, v = [0] * n, [0] * n, [0] * n

# 最大値を更新する
for i in range(n):
    l[i], r[i], v[i] = map(int,input().split())
    #for j in range(l[i], r[i] + 1):
        #dp[j] = max(dp[j], v)

for i in range(n): # i番目の調味料
    for j in range(w + 1): # 価値が j であるとき
        if l[i] <= j and j <= r[i]: # 調味料を選ぶとき
            dp[i + 1][j] = max(dp[i][j - l[i]] + v[i], dp[i][j])
        else: # 調味料を選ばないとき
            dp[i + 1][j] = dp[i][j]


print(*dp,sep = "\n")
if dp[w] == 0:
    print(-1)
else:
    print(dp[w])