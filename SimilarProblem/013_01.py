n, x, y = map(int,input().split())
x, y = x - 1, y - 1

num = [0] * (n - 1)
for i in range(n - 1):
    for j in range(i + 1, n):
        num[min(j - i, abs(x - i) + 1 + abs(j - y), abs(y - i) + 1 + abs(j - x))] += 1

for i in range(n - 2):
    print(num[i + 1])
print(0)