n = int(input())
a = list(map(int,input().split()))

ans = 0
num = [0] * 200
for i in range(n):
    num[a[i] % 200] += 1

for i in range(200):
    ans += num[i] * (num[i] - 1) // 2

print(ans)