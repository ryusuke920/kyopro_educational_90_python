n = int(input())
a = list(map(int,input().split()))

# ０が含まれている場合
if 0 in a:
    exit(print(0))

ans = 1
for i in range(n):
    ans *= a[i]
    if ans > 10 ** 18:
        print(-1)
        break
else:
    print(ans)