from itertools import combinations, permutations

n, m, p, q, r = map(int,input().split())
score = [[0] * m for _ in range(n)]
for _ in range(r):
    x, y, z = map(int,input().split())
    score[x - 1][y - 1] = z

ans = 0
# n人の女子のうち、p人を選ぶ
for comb in combinations(range(n), p):
    man = [0] * m
    # 何人目の女性か
    for woman in comb:
        for i in range(m):
            man[i] += score[woman][i]
    man.sort(reverse=True)
    # 男の幸福度の高い上位q人を選ぶ
    ans = max(ans, sum(man[:q]))

print(ans)