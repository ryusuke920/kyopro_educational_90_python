from itertools import product
n, m = map(int,input().split())
a, b = [0] * m, [0] * m
for i in range(m):
    a[i],b[i] = map(int,input().split())

k = int(input())
c, d = [0] * k, [0] * k
for i in range(k):
    c[i],d[i] = map(int,input().split())
 
ans = 0
for i in product([0, 1], repeat = k):
    num = []
    cnt = 0
    for j in range(k):
        if i[j] == 1:
           num.append(c[j])
        else:
            num.append(d[j])
    for l in range(m):
        if (a[l] in num and b[l] in num):
            cnt += 1
    ans = max(ans,cnt)
print(ans)