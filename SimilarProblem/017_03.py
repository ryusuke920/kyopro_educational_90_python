n = int(input())
ans = 0
cnt = []

for i in range(2, min(10 ** 5 + 100, n + 1)):
    j = 2
    while i ** j <= n:
        cnt.append(i ** j)
        ans += 1
        j += 1

cnt = set(cnt)
print(n - len(cnt))