def divisors(n):
    divisor = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor.append(i)
            if i != n // i:
                divisor.append(n // i)
    return divisor

k = int(input())
ans = 0
for a in divisors(k):
    for b in divisors(k // a):
        c = k // (a * b)
        if a <= b <= c:
            ans += 1

print(ans)