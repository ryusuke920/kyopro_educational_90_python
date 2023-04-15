N = int(input())
W = list(map(int, input().split()))
B = list(map(int, input().split()))

# 白の最大値 = 50, 青の最大値: b + w * (w + 1) / 2 := 1300
# grundy[i][j] := 白が i 個, 青が j 個の grundy 数
grundy = [[-1] * 1400 for _ in range(51)]
grundy[0][0] = 0
grundy[0][1] = 0

for w in range(51):
    for b in range(1300):
        check = set()
        if w >= 1 and grundy[w - 1][b + w] != -1:
            check.add(grundy[w - 1][b + w])
        if b >= 2:
            for k in range(1, b // 2 + 1):
                if grundy[w][b - k] != -1:
                    check.add(grundy[w][b - k])
        i = 0
        while True:
            if i not in check:
                grundy[w][b] = i
                break
            i += 1

ans = 0
for i in range(N):
    ans ^= grundy[W[i]][B[i]]

if ans == 0:
    print('Second')
else:
    print('First')