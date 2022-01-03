n = int(input())
s = input()

ans = 0
for i in range(1000):
    password = f'{i:03}'
    lock = 0 # 何桁目を見ているか
    for j in s:
        if j == password[lock]:
            lock += 1
        if lock == 3:
            ans += 1
            break

print(ans)