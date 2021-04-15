from bisect import bisect_left
n = int(input())
a = list(map(int,input().split()))
q = int(input())
b = [int(input()) for _ in range(q)]
a.sort()

for i in range(q):
    x = bisect_left(a, b[i])
    if x == 0:
        print(a[0] - b[i])
    else:
        print(min(b[i] - a[x - 1], a[x] - b[i]))