n, m = map(int,input().split())
ans = [0] * n
for i in range(m):
    a, b = map(int,input().split())
    if a < b:
        ans[b - 1] += 1
    else:
        ans[a - 1] += 1

# 自分より小さい頂点が１つしかないものをカウントする
print(ans.count(1))