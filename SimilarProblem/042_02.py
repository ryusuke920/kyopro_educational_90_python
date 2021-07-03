from collections import Counter
s = input()
x = Counter(s)
if len(s) <= 2:
    if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
        exit(print("Yes"))
    else:
        exit(print("No"))

for i in range(0, 1000, 8):
    if len(str(i)) <= 2:
        i = str(i)
        i += "0"
    y = Counter(str(i))
    if len(y - x) == 0:
        exit(print("Yes"))

print("No")