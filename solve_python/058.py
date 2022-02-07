def DigitSum(num: int) -> int:
    '''int 型の桁和を求める'''
    digit_sum = 0

    while num > 0:
        digit_sum += num % 10
        num //= 10

    return digit_sum

def calc(k: int) -> int:
    return (DigitSum(k) + k) % 10 ** 5

n, K = map(int, input().split())

# dob[k][i] := iから 2**k 先のDP
dob = [[0] * 10 ** 5 for _ in range(60)]

for i in range(10 ** 5):
    dob[0][i] = calc(i)

for k in range(1, 60):
    for i in range(10 ** 5):
        dob[k][i] = dob[k - 1][dob[k - 1][i]]

now = n
for i in range(60):
    if K >> i & 1:
        now = dob[i][now]

print(now)