n = int(input())

ans = set()
for a in range(2, int(n ** 0.5) + 1):
    b = 2
    while a ** b <= n:
        ans.add(a ** b)
        b += 1

print(n - len(ans))