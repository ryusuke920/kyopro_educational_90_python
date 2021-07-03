l, r = map(int, input().split())

def count_number(number: int) -> int:
    digit, cnt = 1, 0
    while True:
        under = 10 ** (digit - 1) - 1
        top = min(number, 10 ** digit - 1)
        cnt += ((top * (top + 1) - under * (under + 1)) // 2) * digit

        if number <= 10 ** digit - 1:
            return cnt
        digit += 1

print((count_number(r) - count_number(l - 1)) % (10 ** 9 + 7))