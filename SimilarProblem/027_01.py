from collections import defaultdict

d = defaultdict(int)
max_cnt = 0
for _ in range(int(input())):
    s = input()
    d[s] += 1
    max_cnt = max(max_cnt, d[s])

ans = []
for k, v in d.items():
    if v == max_cnt:
        ans.append(k)

print(*sorted(ans), sep='\n')