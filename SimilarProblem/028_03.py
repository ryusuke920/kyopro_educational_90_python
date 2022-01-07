while True:
    n = int(input())
    if n == 0:
        exit()

    num = [0] * 10 ** 5
    for _ in range(n):
        x, y = input().split()
        h1, m1, s1 = x.split(":")
        h2, m2, s2 = y.split(":")
        time1 = int(h1) * 3600 + int(m1) * 60 + int(s1)
        time2 = int(h2) * 3600 + int(m2) * 60 + int(s2)
        num[time1] += 1
        num[time2] -= 1

    for i in range(len(num) - 1):
        num[i + 1] += num[i]
    
    print(max(num))