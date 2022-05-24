def divisors(n: int) -> list:
    divisor = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor.append(i)
            if i != n // i:
                divisor.append(n // i)

    divisor.sort()
    return divisor

n = int(input())
k = int(input())

div = divisors(k)
ans = 0
for ac in div:
    bd = k // ac
    
    if ac > 2 * n or bd > 2 * n:
        continue

    if ac <= n + 1:
        ac -= 1
    else:
        ac = 2 * n - ac + 1

    if bd <= n + 1:
        bd -= 1
    else:
        bd = 2 * n - bd + 1
    
    ans += ac * bd

print(ans)