n = int(input())
a = [sum(list(map(int,input().split()))) for _ in range(n)]
ans = 1
mod = 10 ** 9 + 7

for i in a:
    ans *= i
    ans %= mod
print(ans)