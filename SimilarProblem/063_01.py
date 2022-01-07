n = int(input())

ans = 10 ** 18
for b in range(100):
    a = n // 2 ** b
    c = n - a * 2 ** b
    if c >= 0:
        ans = min(ans, a + b + c)

print(ans)