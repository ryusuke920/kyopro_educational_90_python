from bisect import bisect_right

def solve() -> None:
    n = int(input())
    if n == 1:
        print("?", 1)
        print("!", int(input()))
        return
    
    mid = bisect_right(fib, n)
    a = [-1] * (n + 1) + [0] * (fib[mid] - n)
    d = 0
    l, r = fib[mid - 2], fib[mid - 1]
    for i in range(mid - 2):
        l = fib[mid - 2 - i] + d
        r = fib[mid - 2 - i] + fib[mid - 2 - i - 1] + d
        if a[l] < 0:
            print("?", l)
            a[l] = int(input())
        if a[r] < 0:
            print("?", r)
            a[r] = int(input())
        if a[l] < a[r]:
            d = l
    
    if a[l] < a[r]:
        print("!", a[r])
    else:
        print("!", a[l])


fib = [1, 1]
for i in range(20):
    fib.append(fib[-1] + fib[-2])


for _ in range(int(input())):
    solve()