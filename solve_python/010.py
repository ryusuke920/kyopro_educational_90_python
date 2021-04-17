n = int(input())
c, p = [0] * n, [0] * n
for i in range(n):
    c[i], p[i] = map(int,input().split())
one = [0] * n
two = [0] * n
if c[0] == 1:
    one[0] = p[0]
else:
    two[0] = p[0]
for i in range(n - 1):
    if c[i + 1] == 1:
        one[i + 1] += one[i] + p[i + 1]
        two[i + 1] += two[i]
    else:
        one[i + 1] += one[i]
        two[i + 1] += two[i] + p[i + 1]

q = int(input())
for i in range(q):
    l, r = map(int,input().split())
    l, r = l - 1, r - 1 # 0index
    if l == 0 and r == 0:
        print(one[0], two[0])
    elif l == 0 and r != 0:
        print(one[r], two[r])
    else:
        print(one[r] - one[l - 1], two[r] - two[l - 1])