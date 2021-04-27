n = int(input())
s = input()
mod = 10 ** 9 + 7
a = at = atc = atco = atcod = atcode = atcoder = 0
for i in s:
    if i == "a":
        a += 1
    elif i == "t":
        at += a
    elif i == "c":
        atc += at
    elif i == "o":
        atco += atc
    elif i == "d":
        atcod += atco
    elif i == "e":
        atcode += atcod
    elif i == "r":
        atcoder += atcode

print(atcoder % mod)