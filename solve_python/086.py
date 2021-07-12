def solve(shift):
    tmp = 2 ** n
    for bit in range(tmp):
        for x, y, z, w in p:
            if (bit >> x & 1) | (bit >> y & 1) | (bit >> z & 1) != (w >> shift & 1):
                tmp -= 1
                break

    return tmp

n, q = map(int,input().split())
p = []
for _ in range(q):
    x, y, z, w = map(int,input().split())
    p.append((x - 1, y - 1, z - 1, w))

ans = 1
mod = 10 ** 9 + 7
for i in range(60):
    ans *= solve(i)
    ans %= mod

print(ans)