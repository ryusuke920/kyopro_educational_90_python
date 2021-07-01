n, m = map(int,input().split())

gate = [1, n]
for _ in range(m):
    l, r = map(int,input().split())
    gate[0] = max(gate[0], l)
    gate[1] = min(gate[1], r)

print(max(gate[1] - gate[0] + 1, 0))