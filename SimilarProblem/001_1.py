import sys
input = sys.stdin.readline
import math
n, m = map(int,input().split())
x, y, r = [0] * (n + m), [0] * (n + m), [0] * n
for i in range(n):
    x[i], y[i], r[i] = map(int,input().split())
for i in range(m):
    x[i + n], y[i + n] = map(int,input().split())

a = set()
for i in range(n + m):
    for j in range(n + m):
        if i <= n - 1 and j <= n - 1: continue # nどうし
        if i <= n - 1 and j >= n: # nとmのペア
            a.add(abs(math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) - r[i]))
        if i >= n and j >= n:# mどうし
            a.add(math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) / 2)

if len(a) == 0:
    print(min(r))
else:
    a = list(a)
    a.sort()
    a = a[1:]
    print(min(a))