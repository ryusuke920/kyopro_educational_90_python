n, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

num = 0
for i in range(n):
    num += abs(a[i] - b[i])

if abs(num - k) % 2 == 0 and num <= k:
    print("Yes")
else:
    print("No")