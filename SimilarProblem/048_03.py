n = int(input())
s = input()
t = input()

x, y = [], []
for i in range(n):
    if s[i] == "0":
        x.append(i)
    if t[i] == "0":
        y.append(i)

if len(x) != len(y):
    exit(print(-1))

cnt = 0
for i in range(len(x)):
    if x[i] == y[i]:
        cnt += 1

print(len(x) - cnt)