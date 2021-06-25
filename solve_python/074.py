n = int(input())
s = input()
num = [ord(i) - 97 for i in s]

ans = 0
for i, j in enumerate(num):
    if j == 0: continue
    if j == 1:
        ans += 2 ** i
    elif j == 2:
        ans += 2 ** (i + 1)
print(ans)