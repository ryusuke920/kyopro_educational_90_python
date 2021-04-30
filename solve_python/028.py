n = int(input())
l = 1001
s = [[0] * l for _ in range(l)]
ans = [0] * (n + 1) # 紙が k 枚重なっている部分の面積

for _ in range(n):
    lx, ly, rx, ry = map(int,input().split())
    k = rx - lx # 長方形の横幅
    for i in range(ry - ly):
        s[i + ly][lx] += 1
        s[i + ly][lx + k] -= 1

# いもす法で累積和を取っていく
for i in range(l):
    for j in range(l - 1):
        s[i][j + 1] += s[i][j]

for i in range(l):
    for j in range(l):
        ans[s[i][j]] += 1

ans = ans[1:] # 欲しいのは 1, 2 ... N なので 0 番目はスキップ
print(*ans,sep = "\n")