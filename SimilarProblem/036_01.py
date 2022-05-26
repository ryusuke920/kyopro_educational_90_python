n = int(input())

z, w = [], []
for _ in range(n):
    x, y = map(int, input().split())
    z.append(x + y)
    w.append(x - y)

print(max(max(z) - min(z), max(w) - min(w)))