"""
t = 1 ... xを上に入れる
t = 2 ... xを下に入れる
t = 3 ... 上からx番目のカードを出力
"""
Q = int(input())
from collections import deque
q = deque()
for i in range(Q):
    t, x = map(int,input().split())
    if t == 1:
        q.appendleft(x)
    elif t == 2:
        q.append(x)
    elif t == 3:
        print(q[x - 1])