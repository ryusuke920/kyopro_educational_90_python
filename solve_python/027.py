n = int(input())
name, ans = set(), []
for i in range(n):
    s = input()
    if s not in name:
        ans.append(i + 1)
    name.add(s)
print(*ans, sep = "\n")