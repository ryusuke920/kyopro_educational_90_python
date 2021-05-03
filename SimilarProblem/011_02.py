n = int(input())
a, b = [None] * n, [None] * n
ab = []

for i in range(n):
    a[i], b[i] = map(int, input().split())
    ab.append([a[i], a[i] + b[i], 2 * a[i] + b[i]])

num_a = sum(a) # 青木君
num_b = 0 # 高橋君
cnt = 0
ab = sorted(ab, reverse=True, key=lambda x: x[2])
if len(ab) == 1:
    print(1)
else:
    for i in range(n):
        num_a -= ab[i][0]
        num_b += ab[i][1]
        cnt += 1
        if num_a < num_b:
            exit(print(cnt))