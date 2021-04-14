from itertools import product
n = int(input())
ans = []

if n % 2 == 0: # 奇数のときは正しいカッコ列を生成できない
    for i in product([0, 1], repeat = n): # 0 -> （ , 1 -> ）
        if i.count(1) == n // 2: # 0, 1の個数が同じ時に判定を始める
            zero_count = 0
            Bool = True
            word = ""
            for j in range(len(i)):
                if i[j] == 0:
                    zero_count += 1
                elif i[j] == 1:
                    if zero_count >= 1: # 0の個数が１個以上ないと正しい文字列にならない
                        zero_count -= 1
                    else:
                        Bool = False
                word += str(i[j])
            if Bool:
                x = word.replace("0", "(")
                y = x.replace("1", ")")
                ans.append(y)

ans.sort()
print(*ans ,sep = "\n")