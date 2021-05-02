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
ide_ele = 0 # 初期値（単位元）の設定

class LazySegmentTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.data = [ide_ele] * 2 * self.num
        self.lazy = [None] * 2 * self.num
        for i in range(n):
            self.data[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1])

    def gindex(self, l, r):
        l += self.num
        r += self.num
        lm = l >> (l & -l).bit_length()
        rm = r >> (r & -r).bit_length()
        while l < r:
            if l <= lm:
                yield l
            if r <= rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1

    def propagates(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[2 * i] = v
            self.lazy[2 * i + 1] = v
            self.data[2 * i] = v
            self.data[2 * i + 1] = v
            self.lazy[i] = None

    def update(self, l, r, x):
        *ids, = self.gindex(l, r)
        self.propagates(*ids)
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                self.lazy[l] = x
                self.data[l] = x
                l += 1
            if r & 1:
                self.lazy[r - 1] = x
                self.data[r - 1] = x
            r >>= 1
            l >>= 1
        for i in ids:
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1])

    def query(self, l, r):
        *ids, = self.gindex(l, r)
        self.propagates(*ids)
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.data[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.data[r - 1])
            l >>= 1
            r >>= 1
        return res

w, n = map(int,input().split()) # 配列の長さ・クエリ数
a = [0] * w
seg = LazySegmentTree(a, segfunc, ide_ele)
for i in range(n):
    l, r = map(int,input().split())
    cnt = seg.query(l - 1, r) # l は0index, r は1index (lからrまでのうちの最大値を取得する)
    seg.update(l - 1, r, cnt + 1) # lからrまでの区間をその最大値 +1 に書き換える
    print(cnt + 1)