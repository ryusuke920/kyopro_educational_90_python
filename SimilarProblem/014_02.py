n = int(input())
ab = [list(map(int,input().split())) for _ in range(n)]
ab.sort(key = lambda x : x[1])
ans = 0
for i in range(n):
    ans += ab[i][0]
    if ans > ab[i][1]:
        print("No")
        break
else:
    print("Yes")