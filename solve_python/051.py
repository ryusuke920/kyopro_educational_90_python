from itertools import product
from bisect import bisect_left, bisect_right

def bit_search(A: list, l: int):
    "配列, 配列の長さ"
    num_list = [[] for _ in range(l + 1)] # 0 ~ lまでのl + 1個の配列を用意する
    for i in product([0, 1], repeat = l):
        num = 0
        for j in range(l):
            if i[j] == 1:
                num += A[j]
        num_list[i.count(1)].append(num)
    
    # 昇順にする
    for i in range(len(num_list)):
        num_list[i].sort()
    
    return num_list

n, k, p = map(int,input().split())
a = list(map(int,input().split()))
left, right = a[:n // 2], a[n // 2:] # ２つのグループに分割する

left_num = bit_search(left, len(left)) # leftの配列の和を取る
right_num = bit_search(right, len(right)) # rightの配列の和を取る

ans = 0
for i in range(len(left_num)):
    num = k - i # どこのグループから持ってくるか
    for j in range(len(left_num[i])):
        value = p - left_num[i][j] # 残りの値段
        if num < 0 or value < 0: continue # 個数が負、値段が負の場合は飛ばす
        if not (0 <= num <= len(right_num) - 1): continue # 配列街参照対策
        x = bisect_right(right_num[num], value)
        ans += x
print(ans)