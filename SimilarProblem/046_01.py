n = int(input())
s = [str(input()) for _ in range(n)]

cnt = [0] * 5
for i in range(n):
    if s[i][0] == "M":
        cnt[0] += 1
    elif s[i][0] == "A":
        cnt[1] += 1
    elif s[i][0] == "R":
        cnt[2] += 1
    elif s[i][0] == "C":
        cnt[3] += 1
    elif s[i][0] == "H":
        cnt[4] += 1

ans = 0
ans += cnt[0] * cnt[1] * cnt[2]
ans += cnt[0] * cnt[1] * cnt[3]
ans += cnt[0] * cnt[1] * cnt[4]
ans += cnt[0] * cnt[2] * cnt[3]
ans += cnt[0] * cnt[2] * cnt[4]
ans += cnt[0] * cnt[3] * cnt[4]
ans += cnt[1] * cnt[2] * cnt[3]
ans += cnt[1] * cnt[2] * cnt[4]
ans += cnt[1] * cnt[3] * cnt[4]
ans += cnt[2] * cnt[3] * cnt[4]

print(ans)