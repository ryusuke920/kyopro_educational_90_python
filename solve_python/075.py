def factorization(n):
    arr = []
    tmp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            arr.append([i, cnt])
    if tmp != 1:
        arr.append([tmp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr

num = sum(i[1] for i in factorization(int(input())))
if num == 1:
    print(0)
else:
    i = 0
    while True:
        if num <= 2 ** i:
            break
        i += 1
        ans = 2 ** i
    print(i)