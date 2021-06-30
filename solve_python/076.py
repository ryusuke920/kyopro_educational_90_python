from bisect import bisect_left
n = int(input())
a = list(map(int,input().split()))

# 入力は整数なので10分の1も整数でなければNoになる
if sum(a) % 10 != 0:
    exit(print("No"))

# 目標となる1/10の値
num = sum(a) // 10

# 前からの累積和と後ろからの累積和
x, y = [a[0]], [a[-1]]
for i in range(n - 1):
    x.append(a[i + 1] + x[-1])
    y.append(a[-2 - i] + y[-1])

for i in range(n):
    # 目的の大きさと一致した場合
    if x[i] == num:
        exit(print("Yes"))
    # 目的の大きさより多く選んでしまった場合
    elif x[i] > num:
        j = bisect_left(x, x[i] - num) # 余分な分を二分探索
        if x[i] - x[j] == num:
            exit(print("Yes"))
    # 目的の大きさより小さい場合は後ろから持ってくる
    elif x[i] < num:
        j = bisect_left(y, num - x[i]) # 後ろから二分探索
        if x[i] + y[j] == num:
            exit(print("Yes"))

print("No")