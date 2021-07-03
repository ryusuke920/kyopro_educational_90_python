n = int(input())
h = list(map(int,input().split()))

dp = [0, abs(h[0] - h[1])]
for i in range(n - 2):
    dp.append(min(dp[-2] + abs(h[i] - h[i + 2]), dp[-1] + abs(h[i + 1] - h[i + 2])))

print(dp[-1])