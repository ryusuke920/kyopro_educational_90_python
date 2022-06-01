n = int(input())
b = [int(input()) for _ in range(n - 1)]

# g[i] := i の直属の部下
g = [[] for _ in range(n + 1)]
for i in range(n - 1):
    num = i + 2 # 社員番号
    top = b[i] # 上司の番号
    g[top].append(num)

# money[i] := 社員 i の給料
money = [0] * (n + 1)
for i in reversed(range(1, n + 1)):
    # 部下がいない場合
    if len(g[i]) == 0:
        money[i] = 1
    elif len(g[i]) == 1:
        child = g[i][0]
        money[i] = money[child] * 2 + 1
    else:
        children = []
        for child in g[i]:
            children.append(money[child])
        money[i] = max(children) + min(children) + 1
    
print(money[1])