n = int(input())
a, b = [0] * n, [0] * n
num = [0] * (10 ** 6 + 1)

for i in range(n):
    a[i], b[i] = map(int,input().split())
    num[a[i]] += 1
    if b[i] == 10 ** 6: continue
    num[b[i] + 1] -= 1

for i in range(len(num) - 1):
    num[i + 1] += num[i]

ans = 0
for i in range(len(num)):
    ans = max(ans, num[i])

print(ans)