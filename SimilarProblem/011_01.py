n = int(input())
num = [0] * n
for i in range(n):
    x, l = map(int,input().split())
    num[i] = (x - l, x + l)
num.sort(key = lambda x: x[-1])

ans = 0
x = -float("inf")
for a, b in num:
    if x <= a:
        ans += 1
        x = b
print(ans)