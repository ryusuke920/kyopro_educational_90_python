a, b, c, x, y = map(int,input().split())
ans = 0
if a + b <= c * 2:
    print(a * x + b * y)
else:
    num = c * min(x, y) * 2
    if x < y:
        print(num + min((y - x) * c * 2, (y - x) * b))
    else:
        print(num + min((x - y) * c * 2, (x - y) * a))