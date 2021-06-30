n = int(input())
ans, i, cnt, num = [], 1, 1, 2

while True:
    while i < num:
        ans.append(cnt)
        i += 1
    cnt += 1
    i = num
    num = i * 2
    if i > n:
        break

ans = ans[:n]

print(*ans)