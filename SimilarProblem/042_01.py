s = input()
digit = 0
for i in range(len(s)):
    digit += int(s[i])

if digit % 3 == 0:
    exit(print(0))
else:
    for i in range(len(s)):
        if (digit - int(s[i])) % 3 == 0 and len(s) != 1:
            exit(print(1))
    for i in range(len(s) - 1):
        for j in range(i+1,len(s)):
            if (digit - int(s[i]) - int(s[j])) % 3 == 0 and len(s) != 2:
                exit(print(2))

print(-1)